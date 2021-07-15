import bisect 
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        
        n = len(A)
        zeros = 0
        dp = [0]*n
        ans = 0

        for i in range(n):
            if A[i]==0:
                zeros+=1
            dp[i]=zeros
        # print(dp)
        for i in range(n):
            val = dp[i]
            if A[i]==1:
                right = bisect.bisect_left(dp,val+K+1)
            else:
                right = bisect.bisect_left(dp,val+K)
            # print(i,right)
            delta = right-i
            ans = max(ans,delta)
            # print(i,ans,right)
        return ans 
