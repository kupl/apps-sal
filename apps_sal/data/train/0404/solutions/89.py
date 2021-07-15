from functools import lru_cache 
class Solution(object):
    def largestSumOfAverages(self, A, K):
        l = len(A)
        @lru_cache(None)
        def dp(n, k):
            if n < k: return 0
            if k == 1: return sum(A[:n])/float(n)
            cursum, ans = 0, 0
            for i in range(n-1, -1, -1):
                cursum += A[i]
                ans = max(ans, dp(i, k-1) + cursum/float(n-i))
            return ans
        return dp(l, K)

