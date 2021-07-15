class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
#         fMax = [A[0]]
#         for num in A[1:]:
#             fMax.append(max(fMax[-1], num))
        aLen = len(A)
#         bMax = [num for num in A]
#         for i in range(aLen-2, -1, -1):
#             bMax[i] = max(bMax[i], bMax[i+1])
        
#         ans = 0
#         for i in range(aLen-1):
#             ans = max(ans, (i+1)*fMax[i] + (aLen-i-1)*bMax[i+1])
#         return ans
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
