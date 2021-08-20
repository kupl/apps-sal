class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        num_odd_numbers = 0
        foo = 0
        left = 0
        right = 0
        count = 0
        num_nice_arrays = 0
        while right < len(nums):
            r_n = nums[right]
            if r_n % 2 == 1:
                count = 0
                num_odd_numbers += 1
            while num_odd_numbers == k:
                l_n = nums[left]
                if l_n % 2 == 1:
                    num_odd_numbers -= 1
                left += 1
                count += 1
            num_nice_arrays += count
            right += 1
        return num_nice_arrays
