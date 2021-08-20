class Solution:

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = [float('-inf')] * len(stoneValue)
        self.presum = [0] * (len(stoneValue) + 1)
        for (idx, num) in enumerate(stoneValue[::-1]):
            self.presum[len(stoneValue) - idx - 1] = self.presum[len(stoneValue) - idx] + num
        self.presum.pop()
        alice_score = self.helper(stoneValue, 0, dp)
        if alice_score > sum(stoneValue) - alice_score:
            return 'Alice'
        elif alice_score < sum(stoneValue) - alice_score:
            return 'Bob'
        else:
            return 'Tie'

    def helper(self, nums, start, dp):
        if dp[start] != float('-inf'):
            return dp[start]
        if start == len(nums) - 1:
            dp[start] = nums[start]
            return nums[start]
        if start == len(nums) - 2:
            dp[start] = max(self.presum[start], nums[start])
            return dp[start]
        if start == len(nums) - 3:
            dp[start] = max(self.presum[start], self.presum[start] - self.helper(nums, start + 1, dp), self.presum[start] - self.helper(nums, start + 2, dp))
            return dp[start]
        num1 = self.presum[start] - self.helper(nums, start + 1, dp)
        num2 = self.presum[start] - self.helper(nums, start + 2, dp) if start + 2 < len(nums) else float('-inf')
        num3 = self.presum[start] - self.helper(nums, start + 3, dp) if start + 3 < len(nums) else float('-inf')
        dp[start] = max(num1, num2, num3)
        return dp[start]
