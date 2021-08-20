class Solution:

    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        n = len(nums)
        pref_sum = [0 for _ in range(n + 1)]
        for i in range(n):
            pref_sum[i + 1] = pref_sum[i] + nums[i]
        dp = collections.defaultdict(lambda: -1)
        cur_max = 0
        dp[0] = 0
        for pref in range(1, n + 1):
            cur_max = max(cur_max, dp[pref_sum[pref] - target] + 1)
            dp[pref_sum[pref]] = cur_max
        return cur_max
