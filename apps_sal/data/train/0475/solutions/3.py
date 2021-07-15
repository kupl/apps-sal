class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        mod = 10**9+7
        dp = [0]
        for i in range(n):
            total = 0
            for j in range(i,n):
                total += nums[j]
                dp.append(total)
        
        dp.sort()
        for i in range(1,len(dp)):
            dp[i] += dp[i-1]
            dp[i] %= mod
        
        return (dp[right]-dp[left-1])%mod
