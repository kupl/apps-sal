class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        nums.sort()

        res = 0
        l = 0
        n = len(nums)
        pow2 = [1]
        for x in range(1, n + 1):
            pow2.append(pow2[-1] * 2 % MOD)

        j = n - 1
        for i in range(n):
            while j and nums[i] + nums[j] > target:
                j -= 1
            if i <= j and nums[i] + nums[j] <= target:
                res += pow2[j - i]
                res %= MOD
        return res

        MODULO = 10 ** 9 + 7
        nums.sort()

        res = 0
        l = 0
        n = len(nums)

        while l < n and nums[l] * 2 <= target:
            r = l
            while r < n and nums[l] + nums[r] <= target:
                r += 1
            if l <= r < n:
                if l == r and nums[l] + nums[r] <= target:
                    res += 1
                elif l < r and nums[l] + nums[r - 1] <= target:
                    res += (2 ** (r - l - 1)) % MODULO
            elif r == n and nums[l] + nums[r - 1] <= target:
                r -= 1
                res += (2 ** (r - l)) % MODULO
            l += 1
        return res % MODULO
