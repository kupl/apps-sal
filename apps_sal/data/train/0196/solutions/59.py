class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        # On
        n = len(A)
        total = A[0]
        curmax = A[0]
        curmin = A[0]
        maxsum = curmax
        minsum = curmin
        for i in range(1, n):
            curmax = max(curmax + A[i], A[i])
            maxsum = max(maxsum, curmax)
            curmin = min(curmin + A[i], A[i])
            minsum = min(minsum, curmin)
            total += A[i]
        # get maxsum and minsum
        # total-minsum and maxsum
        if total == minsum:
            return maxsum
        else:
            return max(maxsum, total - minsum)


#         dp=[0]*n
#         optsum=[A[0]]*n
#         pre=A[0]
#         dp[0]=A[0]
#         first=dp[0]
#         for i in range(1,n):
#             dp[i]=max(dp[i-1]+A[i],A[i])
#             first=max(first,dp[i])

#             pre+=A[i]
#             if pre>optsum[i-1]:
#                 optsum[i]=pre
#             else:
#                 optsum[i]=optsum[i-1]
#         # get second case now
#         #print(optsum)
#         pre=0
#         for j in range(n-1,0,-1):
#             first=max(first,pre+A[j]+optsum[j-1])
#             pre+=A[j]

#         return first
