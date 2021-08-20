class Solution:

    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dp = [nums[0]]
        decrease = collections.deque([0])
        for (i, num) in enumerate(nums[1:], 1):
            if decrease and i - decrease[0] > k:
                decrease.popleft()
            val = max(num, dp[decrease[0]] + num)
            dp.append(val)
            while decrease and dp[decrease[-1]] <= val:
                decrease.pop()
            decrease.append(i)
        return max(dp)
