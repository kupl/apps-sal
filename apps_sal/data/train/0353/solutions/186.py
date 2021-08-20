class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        j = len(nums) - 1
        i = 0
        while i <= j:
            if nums[i] + nums[j] > target:
                j -= 1
            else:
                res += 2 ** (j - i) % (10 ** 9 + 7)
                i += 1
        return res % (10 ** 9 + 7)
