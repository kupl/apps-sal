class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = 10 ** 9 + 7
        nums.sort()
        result = 0
        (i, j) = (0, len(nums) - 1)
        while i <= j:
            cur_sum = nums[i] + nums[j]
            if cur_sum <= target:
                result += pow(2, j - i, mod)
                i += 1
            else:
                j -= 1
        return result % mod
