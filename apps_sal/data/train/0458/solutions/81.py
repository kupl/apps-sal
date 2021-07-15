class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        need = sum(nums)%p
        dp = {0: -1}
        cumsum = 0
        res = float('inf')
        for i in range(len(nums)):
            cumsum = (cumsum + nums[i])%p
            dp[cumsum] = i
            if (cumsum-need)%p in dp:
                res = min(res, i-dp[(cumsum-need)%p])
        return res if res <len(nums) else -1
