import math
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [] 
        for i in range(n):
            dp.append([arr[i], arr[i]])
        for i in range(1, n):
            dp[i][0] = max(dp[i][0], dp[i - 1][0] + arr[i])    
            if i > 1:
                dp[i][1] = max(dp[i][1], max(dp[i-1][1]+arr[i], dp[i-2][0]+arr[i]))   
        ans = -math.inf
        for i in range(n):
            ans = max(ans, max(dp[i][0], dp[i][1]))
        return ans
