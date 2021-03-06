class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        le = len(nums)
        res = 0
        mod = 10 ** 9 + 7
        j = le - 1
        for i in range(le):
            while j >= i and nums[i] + nums[j] > target:
                j -= 1
            if j < i:
                break
            res += pow(2, j - i, mod)
            res %= mod
        return res
