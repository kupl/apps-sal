class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # dynamic programming, store largest subarray including element i with/without deleting
        # let dp[i][0] be the longest subarray of all 1s including i
        # let dp[i][1] be the longest subarray of all 1s with 1 zero including i

        if not nums:
            return 0
        if all(nums):
            return len(nums) - 1  # must delete 1 element

        n = len(nums)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = 1 if nums[0] == 1 else 0
        dp[0][1] = 0

        res = 0
        for i in range(1, n):
            if nums[i] == 1:
                dp[i][0] = dp[i - 1][0] + 1  # dp[i][0] is all 1s, so if nums[i] is a num then increment current all 1s
                dp[i][1] = dp[i - 1][1] + 1  # if we have a 1, then increment 1 deletion by 1
            else:
                dp[i][0] = 0  # not allowed to have a zero for dp[i][0]
                dp[i][1] = dp[i - 1][0]  # if we have a zero, then we are allowed 1 deletion, so ignote current element and hold subarray of all 1s from previous

            res = max(res, dp[i][1], dp[i][0])  # check if max is with the i'th element
        return res
