class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        return self.atMostK(nums, k) - self.atMostK(nums, k - 1)

    def atMostK(self, nums, k):
        count = 0
        left = 0

        for right, right_num in enumerate(nums):
            k -= right_num % 2

            while k < 0:
                k += nums[left] % 2
                left += 1

            count += right - left + 1
        return count
