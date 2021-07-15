from functools import lru_cache
class Solution:
    def minDifficulty(self, A, d):
        # n = len(A)
        # dp, dp2 = [math.inf] * n, [0] * n
        # if n < d: return -1
        # for d in range(d):
        #     stack = []
        #     for i in range(d, n):
        #         dp2[i] = dp[i - 1] + A[i] if i else A[i]
        #         while stack and A[stack[-1]] <= A[i]:
        #             j = stack.pop()
        #             dp2[i] = min(dp2[i], dp2[j] - A[j] + A[i])
        #         if stack:
        #             dp2[i] = min(dp2[i], dp2[stack[-1]])
        #         stack.append(i)
        #     dp, dp2 = dp2, [0] * n
        # return dp[-1]
        
        n = len(A)
        if n < d: return -1
        
        @lru_cache(None)
        def dp(n, d):

            if n < d: return math.inf
            if d == 1: return max(A[:n])          
            return min(dp(t, d - 1) + max(A[t : n]) for t in range(n))
        
        return dp(n, d)
        

