class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        dp=[[0]*2 for i in range(len(arr))]
        if len(arr)==0:
            return 0
        
        dp[0][0]=arr[0]
        dp[0][0]=arr[0]
        maxm=arr[0]
        
        for i in range(1,len(arr)):
            dp[i][0]=max(dp[i-1][0]+arr[i],arr[i])
            dp[i][1]=max(arr[i],dp[i-1][1]+arr[i],dp[i-1][0])
            
            maxm=max(maxm,dp[i][0],dp[i][1])
            
        return maxm
                

