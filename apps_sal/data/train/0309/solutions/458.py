class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        N = len(A)
        dp = [collections.defaultdict(int) for _ in A]
        res = 1
        for i in range(N):
            for j in range(i):
                diff = A[i] - A[j]
                if dp[i][diff] == None: dp[i][diff] = 0
                if dp[j][diff] == None: dp[j][diff] = 0
                
                if dp[j][diff] == 0:
                    dp[i][diff] = 2
                else:
                    dp[i][diff] = dp[j][diff] + 1
                
                res = max(res, dp[i][diff])
        return res
