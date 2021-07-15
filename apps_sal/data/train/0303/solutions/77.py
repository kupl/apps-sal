class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0] * (len(arr)+1)
        for i in range(0, len(arr)):
            m = 0
            for j in range(i, i-k, -1):
                if j < 0:
                    break
                t = max(arr[j:i+1]) * (i - j + 1) + dp[j] 
                if t > m:
                    m = t
            dp[i+1] = m
            
        return dp[-1]
