class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        num_nice = 0
        i = 0
        count = 0
        for num in nums:
            if num & 1:
                k -= 1
                count = 0
            while k == 0:
                k += nums[i] & 1
                count += 1
                i += 1
            num_nice += count
        return num_nice
