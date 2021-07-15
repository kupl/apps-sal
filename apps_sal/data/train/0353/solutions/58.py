class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        mod = 10**9 + 7
        i, n = 0, len(nums)
        pows = [0] * n
        p = 1
        while i < n:
            pows[i] = p
            p = 2 * p
            i += 1
        
        # print(pows)
        # print(nums)
        l, r = 0, n-1
        res = 0
        while l <= r:
            # print(l, r)
            if nums[l] + nums[r] <= target:
                res = (res + pows[r-l]) % mod
                l += 1
            else:
                r -= 1
                
        return int(res)

