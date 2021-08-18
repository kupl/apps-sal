class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:

        N = len(A)

        D = {num: idx for idx, num in enumerate(A)}
        dp = [[2] * N for _ in range(N)]

        for j in range(1, N):
            for i in range(j):
                if A[j] - A[i] in D and D[A[j] - A[i]] < i:
                    dp[i][j] = dp[D[A[j] - A[i]]][i] + 1

        res = max(map(max, dp))
        return res if res > 2 else 0
