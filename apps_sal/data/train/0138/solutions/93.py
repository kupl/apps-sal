class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [[0, 0] for _ in range(len(nums))]
        dp[0] = [int(bool(nums[0] > 0)), int(bool(nums[0] < 0))]
        for idx in range(1, len(nums)):
            if nums[idx] == 0:
                continue
            if nums[idx] > 0:
                dp[idx][0] = dp[idx - 1][0] + 1
                dp[idx][1] = dp[idx - 1][1] + int(dp[idx - 1][1] != 0)
            else:
                dp[idx][0] = dp[idx - 1][1] + int(dp[idx - 1][1] != 0)
                dp[idx][1] = dp[idx - 1][0] + 1
        return max([positive for (positive, _) in dp])
