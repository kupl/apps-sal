class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd_count = tmp_count = j = 0
        final_count = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                odd_count += 1
                tmp_count = 0
            while odd_count == k:
                odd_count -= nums[j] % 2
                j += 1
                tmp_count += 1
            final_count += tmp_count
        return final_count
