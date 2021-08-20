class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.numberOfAtmostK(nums, k) - self.numberOfAtmostK(nums, k - 1)

    def numberOfAtmostK(self, nums, k):
        (l, r, count, res) = (0, 0, 0, 0)
        while r < len(nums):
            if nums[r] % 2 == 1:
                count += 1
            while count > k:
                if nums[l] % 2 == 1:
                    count -= 1
                l += 1
            res += r - l + 1
            r += 1
        return res
