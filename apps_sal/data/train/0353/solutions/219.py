class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        mod = 10 ** 9 + 7
        f = [1] + [0] * (n - 1)
        for i in range(1, n):
            f[i] = f[i - 1] * 2 % mod
        pos = n - 1
        for (i, num) in enumerate(nums):
            while nums[pos] + num > target and pos >= i:
                pos -= 1
            if pos >= i:
                res += f[pos - i]
            else:
                break
        return res % mod
