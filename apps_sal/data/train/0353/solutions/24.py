class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:

        low = 0
        high = len(nums) - 1
        nums.sort()
        if not nums:
            return 0
        total = 0
        while low <= high:
            if nums[low] + nums[high] <= target:
                total += pow(2, high - low, 10**9 + 7)
                low += 1
            else:
                high -= 1
        return total % (10**9 + 7)
