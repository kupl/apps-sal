class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        i = 0
        j = len(nums) - 1
        s = 0
        while i <= j:
            if nums[i] + nums[j] <= target:
                s = (s + 2 ** (j - i)) % (10 ** 9 + 7)
                i += 1
            else:
                j -= 1
        return s
