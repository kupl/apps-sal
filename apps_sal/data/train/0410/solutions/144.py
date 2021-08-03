from collections import defaultdict


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        d = defaultdict(list)
        for integer in range(lo, hi + 1):
            res = integer
            cnt = 0
            while res != 1:
                if res % 2 == 0:
                    res /= 2
                elif res % 2 == 1:
                    res = res * 3 + 1
                cnt += 1
            d[cnt].append(integer)
        keys = sorted(d.keys())
        ans = []
        for key in keys:
            ans += sorted(d[key])
        return ans[k - 1]
