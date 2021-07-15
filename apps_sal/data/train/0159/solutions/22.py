class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:

        dp = collections.deque([(nums[0], 0)])
        ans = nums[0]
        
        for i in range(1, len(nums)):
    
            new = nums[i] + max(0,dp[0][0])
            
            while dp and dp[0][1] <= i-k:
                dp.popleft()            
            
            while dp and new >= dp[-1][0]:
                dp.pop()
            
            dp.append((new, i))
            
            ans = max(ans, new)
    
        return ans

