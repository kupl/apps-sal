class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        maxx = arr[0]
        dp = []
        for i,_ in enumerate(arr[:k]):
            maxx=max(arr[i], maxx)
            dp.append(maxx*(i+1))
            
        for i, _ in enumerate(arr[k::]):
            i+=k
            max_sum = 0
            for j in range(k):
                max_sum = max(
                    max_sum,dp[i-j-1] + (max(arr[i-j:i+1])*(j+1))
                )
                
            dp.append(max_sum)
            
        return dp[-1]
                    
            
        

