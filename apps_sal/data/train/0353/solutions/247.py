class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        (i, j) = (0, len(nums) - 1)
        ans = 0
        mod = 10 ** 9 + 7
        while i <= j:
            if nums[i] + nums[j] > target:
                j -= 1
            else:
                ans += self.fast_pow_mod(2, j - i, mod)
                i += 1
        return ans % mod

    def fast_pow_mod(self, a, b, m):
        ans = 1
        while b != 0:
            if b & 1 == 1:
                ans = ans * a % m
            b >>= 1
            a = a * a % m
        return ans
