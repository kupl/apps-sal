class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp=[0]*len(arr)
        dp[0]=arr[0]
        for i in range(1, len(arr)):
            maxval=arr[i]
            for j in range(i, i-k, -1):
                if j<0:
                    break
                maxval=max(maxval, arr[j])
                temp=dp[j-1] if j-1>=0 else 0
                temp+=maxval*(i-j+1)
                dp[i]=max(dp[i], temp)
        return dp[-1]
