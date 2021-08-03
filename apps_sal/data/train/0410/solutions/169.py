class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        d = {}

        def dp(x):
            if x == 1:
                return 0
            if x % 2:
                t = 3 * x + 1
                if t not in d:
                    d[t] = dp(t)
                return 1 + d[t]
            else:
                t = x // 2
                if t not in d:
                    d[t] = dp(t)
                return 1 + d[t]
        d1 = {}
        for i in range(lo, hi + 1):
            d1[i] = dp(i)
        return sorted(d1, key=lambda x: d1[x])[k - 1]
