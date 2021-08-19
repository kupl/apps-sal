class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        def at_most(nums, k):
            cnts = l = res = 0
            for r in range(len(nums)):
                cnts += nums[r] % 2
                while cnts > k:
                    cnts -= nums[l] % 2
                    l += 1
                res += r - l + 1
            return res
        return at_most(nums, k) - at_most(nums, k - 1)
