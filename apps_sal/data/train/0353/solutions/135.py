class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        count = 0
        mod = 10 ** 9 + 7
        nums.sort()
        while i < len(nums) and j < len(nums):
            while nums[j] + nums[i] > target and i <= j:
                j -= 1
            if nums[j] + nums[i] <= target and i <= j:
                count += 2 ** (j - i)
            i += 1
        return int(count % mod)
