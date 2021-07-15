class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        i = count = nice_count = odd_count = 0
        for j in range(len(nums)):
            if nums[j] % 2 == 1:
                odd_count += 1
                count = 0
            while odd_count == k:
                odd_count -= nums[i] % 2
                i += 1
                count += 1
            nice_count += count
        return nice_count
