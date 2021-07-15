class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        aLen = len(A)
        dp = {}
        def helper(i0):
            if i0 in dp:
                return dp[i0]
            if aLen - i0 <= K:
                dp[i0] = max(A[i0:])*(aLen-i0)
                return dp[i0]
            subAns = 0
            thisMax = A[i0]
            for ki in range(1, K+1):
                thisMax = max(thisMax, A[i0+ki-1])
                subAns = max(subAns, thisMax*ki + helper(i0 +ki))
            dp[i0] = subAns
            return subAns
        return helper(0)
