
class Solution:
    def numSubseq(self, x: List[int], t: int) -> int:
        def bi(lo, hi, val):
            while lo <= hi:
                m = (lo + hi) // 2
                if x[m] <= val:
                    lo = m + 1
                else:
                    hi = m - 1
            return lo - 1
        x.sort()
        l = len(x)
        ans = 0
        for i in range(l):
            if t - x[i] >= x[i]:
                ind = bi(i, l - 1, t - x[i])
                ans += 2**(ind - i)
            else:
                break
        return ans % (10**9 + 7)
