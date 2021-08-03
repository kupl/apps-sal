class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        count = 0

        left = 0
        right = 0

        odd = 0

        while right < len(nums):

            if nums[right] % 2 == 1:
                odd += 1

            while left < right and odd > k:
                if nums[left] % 2 == 1:
                    odd -= 1
                left += 1

            if odd == k:
                count += 1

            i = left
            while i < right and odd == k and nums[i] % 2 == 0:
                count += 1
                i += 1

            right += 1

        return count
