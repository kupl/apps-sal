class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        rr = l = r = res = cnt = 0
        ll = -1
        n = len(nums)
        while r < n:
            x = nums[r]
            if x % 2:
                if ll < l:
                    ll = r
                cnt += 1
            if cnt == k:
                rr = r
                while r < n - 1 and nums[r + 1] % 2 == 0:
                    r += 1
                res += (ll - l + 1) * (r - rr + 1)
                l = ll + 1
                cnt -= 1
                ll += 1
                while ll < n and nums[ll] % 2 == 0:
                    ll += 1
            r += 1
        return res
