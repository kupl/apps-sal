class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        cacheMax=[[0]*len(arr) for i in range(len(arr))]
        for i in range(len(arr)):
            cacheMax[i][i]=arr[i]
        for i in range(1,len(arr)):
            for j in range(max(i-k+1,0),i+1):
                cacheMax[j][i] = max(cacheMax[j][i-1],arr[i])
        
        
        
        
        dp=[0]*(len(arr)+1)
        dp[1]=arr[0]
        for i in range(1,len(arr)):
            for j  in range(max(0,i-k+1),i+1):
                dp[i+1]=max(dp[i+1],dp[j]+cacheMax[j][i]*(i-j+1))
                
            
        return dp[-1]
