class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        sn = sorted(nums)
        ans = 0
        mod = 1000000007
        l = 0
        r = len(nums) - 1
        while l <= r:
            if sn[l] + sn[r] > target:
                r -= 1
                continue
            u = int(pow(2, r - l))
            ans = (ans + u) % mod
            l += 1

        return ans
