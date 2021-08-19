class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        N = len(A)
        arr = [[(0, 0)] * (K + 1) for _ in range(N)]
        prev = 0
        for i in range(N):
            arr[i][1] = (A[i] + prev, A[i])
            prev += A[i]
            for j in range(2, min(i + 2, K + 1)):
                mx = max(arr[i - 1][j - 1][1], A[i])
                s = arr[i - 1][j - 1][0] - arr[i - 1][j - 1][1] * (j - 1) + mx * j
                arr[i][j] = (s, mx)
                prev = max(prev, s)
            # print(prev,arr[i][1:])
        return max(arr[-1][k][0] for k in range(1, K + 1))
