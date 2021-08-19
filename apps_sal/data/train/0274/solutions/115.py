class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return 1
        ans = 1
        minelement = maxelement = nums[0]
        l = 0
        r = 1
        while r < n and l <= r:
            minelement = min(minelement, nums[r])
            maxelement = max(maxelement, nums[r])
            if maxelement - minelement <= limit:
                ans = max(ans, r - l + 1)
            else:
                if minelement == nums[l]:
                    minelement = min(nums[l + 1:r + 1])
                if maxelement == nums[l]:
                    maxelement = max(nums[l + 1:r + 1])
                l += 1
            r += 1
        return ans
