class Solution:

    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        (n, cur_sum, max_sum) = (len(A), 0, 0)
        max_l = [[0, 0] for _ in range(n + 2)]
        for i in range(n):
            cur_sum += A[i]
            if i >= L - 1:
                max_l[i + 1][0] = max(max_l[i][0], cur_sum)
                cur_sum -= A[i - L + 1]
        cur_sum = 0
        for i in range(n - 1, -1, -1):
            cur_sum += A[i]
            if i <= n - L:
                max_l[i + 1][1] = max(max_l[i + 2][1], cur_sum)
                cur_sum -= A[i + L - 1]
        cur_sum = 0
        for i in range(n):
            cur_sum += A[i]
            if i >= M - 1:
                max_sum = max(max_sum, cur_sum + max_l[i - M + 1][0], cur_sum + max_l[i + 2][1])
                cur_sum -= A[i - M + 1]
        return max_sum
