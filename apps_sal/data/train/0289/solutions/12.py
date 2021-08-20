class Solution:

    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        n = len(A)
        run_sum = [0] * (n + 1)
        cur_sum = 0
        for i in range(1, n + 1):
            cur_sum += A[i - 1]
            run_sum[i] = cur_sum
        ans = 0
        for i in range(1, n - L + 2):
            L_sum = run_sum[i + L - 1] - run_sum[i - 1]
            for j in range(1, n - M + 2):
                if i + L - 1 < j or j + M - 1 < i:
                    M_sum = run_sum[j + M - 1] - run_sum[j - 1]
                    ans = max(ans, L_sum + M_sum)
        return ans
