class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp=[0]*len(arr)
        dp[0]=arr[0]
        max1=arr[0]
        for i in range(1,k):
            max1=max(max1,arr[i])
            dp[i]=max1*(i+1)
     
        for i in range(k,len(arr)):
            max1=arr[i]
           
            for j in range(1,k+1):
                dp[i]=max(dp[i],max1*j+dp[i-j])
                max1=max(arr[i-j],max1)
        return dp[-1]
