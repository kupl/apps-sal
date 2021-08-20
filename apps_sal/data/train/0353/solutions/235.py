class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = 10 ** 9 + 7
        nums.sort()
        (i, j) = (0, len(nums) - 1)
        count = 0
        while i <= j:
            while i <= j and nums[i] + nums[j] > target:
                j -= 1
            if i <= j:
                count += pow(2, j - i, mod)
                i += 1
        return count % mod
