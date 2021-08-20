class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        res = 0
        nums.sort()
        i = 0
        j = len(nums) - 1
        while i <= j:
            if nums[i] + nums[j] > target:
                j -= 1
            else:
                res += pow(2, j - i)
                res %= 10 ** 9 + 7
                i += 1
        return res
