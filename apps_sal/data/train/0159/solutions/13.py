class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dp = [nums[0]]
        decrease = collections.deque([0])
        for i, x in enumerate(nums[1:], 1):
            if decrease[0] == i-k-1:
                decrease.popleft()
            tmp = max(x, dp[decrease[0]] + x)
            dp += [tmp]
            while decrease and dp[decrease[-1]] <= tmp:
                decrease.pop()
            decrease += [i]            
        return max(dp)  
