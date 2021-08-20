class Solution:

    def numSubseq(self, nums, target: int) -> int:
        n = len(nums)
        nums.sort()
        res = 0
        mod = 10 ** 9 + 7
        last = n - 1
        t = target / 2
        f = [1] + [0] * (n - 1)
        for i in range(1, n):
            f[i] = f[i - 1] * 2 % mod
        i = 0
        while i < n and nums[i] <= t:
            j = last
            while j >= i and nums[i] + nums[j] > target:
                j -= 1
            last = j
            res += f[j - i]
            i += 1
        return res % 1000000007
