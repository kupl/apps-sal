class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        dp = [[2] * len(A) for i in range(len(A))]
        d = {}
        for i in range(len(A)):
            d[A[i]] = i
        ans = 2
        for i in range(1, len(A)):
            for j in range(i):
                fn = A[i] + A[j]
                if fn in list(d.keys()) and d[fn] > i:
                    length = dp[j][i]
                    dp[i][d[fn]] = max(dp[i][d[fn]], 1 + length)
                    ans = max(ans, dp[i][d[fn]])
        if ans == 2:
            return 0
        return ans
