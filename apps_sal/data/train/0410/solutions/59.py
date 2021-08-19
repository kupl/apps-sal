class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:
        d = dict()
        for i in range(lo, hi + 1):
            res = 0
            x = i
            while i != 1:
                if i % 2 == 1:
                    i = 3 * i + 1
                else:
                    i = i / 2
                res += 1
            d[x] = res
        di = {k: v for (k, v) in sorted(d.items(), key=lambda item: item[1])}
        return list(di.keys())[k - 1]
