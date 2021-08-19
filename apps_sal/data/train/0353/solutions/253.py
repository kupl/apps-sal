from bisect import bisect_right


class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        arr = []
        n = len(nums)
        m = 10 ** 9 + 7
        nums.sort()
        ans = 0
        dp = [0] * n
        if 2 * nums[0] <= target:
            dp[0] = 1
        for i in range(1, n):
            if 2 * nums[i] <= target:
                dp[i] = (2 * dp[i - 1] % m + 1 % m) % m
            elif nums[i] < target:
                index = bisect_right(nums, target - nums[i])
                dp[i] = (dp[i - 1] % m + dp[index - 1] % m + dp[index - 1] % m * (pow(2, i - index, m) - 1)) % m
            else:
                dp[i] = dp[i - 1]
        print(dp)
        return dp[n - 1] % m
