class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        a = nums
        a.sort()
        t = target
        while a and a[-1] > t:
            a.pop()
        ans = 0
        l, h = 0, len(a) - 1
        M = 10 ** 9 + 7
        while l <= h:
            while l <= h and a[h] + a[l] > t:
                h -= 1
            if l <= h and a[h] + a[l] <= t:
                ans += ((1 << (h - l)))
                ans %= M
            l += 1
        return ans
