class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        def at_most(k):
            left = 0
            count = 0
            res = 0
            for right in range(len(nums)):
                count += nums[right] & 1
                while count > k and left <= right:
                    count -= nums[left] & 1
                    left += 1
                res += right - left + 1
            return res
        return at_most(k) - at_most(k - 1)
