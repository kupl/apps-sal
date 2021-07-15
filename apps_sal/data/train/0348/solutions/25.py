class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        if len(arr)==1:
            return arr[0]
        dp=[[0]*2 for i in range(len(arr))]
        dp[0][0]=arr[0]
        for i in range(1,len(arr)):
            dp[i][0]=max(arr[i],dp[i-1][0]+arr[i])
            dp[i][1]=max(dp[i-1][1]+arr[i],dp[i-1][0])
        ans=float('-inf')
        for i in range(len(arr)):
            ans=max(ans,dp[i][0],dp[i][1])
        if ans==0:
            return max(arr)
        return ans
