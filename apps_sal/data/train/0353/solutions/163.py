class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        mod = 10 ** 9 + 7
        (i, j) = (0, n - 1)
        for i in range(n):
            while i <= j and nums[i] + nums[j] > target:
                j -= 1
            if i <= j and nums[i] + nums[j] <= target:
                res += pow(2, j - i)
                res %= mod
        return res
