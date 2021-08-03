class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        le = len(nums)
        res = 0
        mod = 10**9 + 7
        for i in range(le):
            if nums[i] * 2 <= target:
                lo, hi = i, le - 1
                while hi > lo:
                    mid = (hi + lo + 1) // 2
                    if nums[i] + nums[mid] <= target:
                        lo = mid
                    else:
                        hi = mid - 1
                res += pow(2, lo - i, mod)
        return res % mod
