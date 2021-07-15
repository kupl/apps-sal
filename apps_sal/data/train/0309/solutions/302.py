class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        N = len(A) 
        dp = [[2] * N for i in range(N)]
        ans = 0
        for i in range(N):
            pos = {}
            for j in range(i):
                x = 2*A[j] - A[i]
                if x in pos:
                    dp[i][j] = max(dp[i][j], 1 + dp[j][pos[x]])
                ans = max(ans, dp[i][j])
                pos[A[j]] = j
        
        return ans
    
        dp = [dict() for _ in range(N)]
        ret = 1
        for i in range(N):
            for j in range(i + 1, N):
                diff = A[j] - A[i]
                dp[j][diff] = dp[i].get(diff, 1) + 1
                ret = max(ret, dp[j][diff])
        return ret
        # def calc(A):
        #     for i in range(len(A) - 1, -1, -1):
        #         for j in range(i + 1, len(A)):
        #             if A[j] < A[i]:
        #                 continue
        #             diff = A[j] - A[i]
        #             memo[i][diff] = max(memo[i].get(diff, 0), memo[j].get(diff, 1) + 1)
        #             ret = max(ret, memo[i][diff])
        #     return ret
        # 
        # return max(
        #     calc(A), calc(list(reversed(A)))
        # )

