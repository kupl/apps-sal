class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        res, n = 1, len(A)
        dp = [{} for _ in range(n)]
        for i in range(1, n):
            for j in range(i-1, -1, -1):
                d = A[i] - A[j]
                if d in dp[i]: continue
                if d in dp[j]:
                    dp[i][d] = dp[j][d]+1
                else:
                    dp[i][d] = 2 
                res = max(res, dp[i][d])
        # print(dp)        
        return res

