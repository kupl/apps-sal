class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        i = 0
        j = len(nums) - 1
        while i < len(nums):
            if target - nums[i] < nums[i]:
                i = i + 1
                continue
            while j > i:
                if nums[j] + nums[i] <= target:
                    break
                j = j - 1
            res = 2 ** (j - i) + res
            i = i + 1
        return res % (10 ** 9 + 7)
