class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if not nums:
            return 0

        l, r = 0, 0
        n = len(nums)
        ll = 0
        mmin = nums[0]
        mmax = nums[0]
        while l <= r and r < n:
            mmax = max(mmax, nums[r])
            mmin = min(mmin, nums[r])
            if abs(mmax - mmin) <= limit:
                ll = max(ll, r - l + 1)
            else:
                if nums[l] == mmax:
                    mmax = max(nums[l + 1: r + 1])
                if nums[l] == mmin:
                    mmin = min(nums[l + 1:r + 1])

                l += 1
            r += 1

        return ll
