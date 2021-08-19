class Solution:

    def atMostK(self, nums, k):
        start = 0
        end = 0
        count = 0
        for end in range(len(nums)):
            if nums[end] % 2 == 1:
                k -= 1
            while k < 0:
                if nums[start] % 2 == 1:
                    k += 1
                start += 1
            count += end - start + 1
        return count

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        if not nums or len(nums) == 0 or k > len(nums):
            return 0
        odds = 0
        return self.atMostK(nums, k) - self.atMostK(nums, k - 1)
