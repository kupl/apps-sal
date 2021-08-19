class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        d = {}
        for i in range(len(A)):
            d[A[i]] = i
        dp = [[2 for i in range(len(A))] for j in range(len(A))]
        ans = 0
        for j in range(0, len(A)):
            for i in range(0, j):
                if A[j] - A[i] in d and d[A[j] - A[i]] < i:
                    k = d[A[j] - A[i]]
                    dp[i][j] = dp[k][i] + 1
                ans = max(dp[i][j], ans)
        return ans if ans >= 3 else 0
