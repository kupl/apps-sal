class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:

        @lru_cache(None)
        def power(x):
            if x == 1:
                return 0
            return 1 + power(x * 3 + 1) if x & 1 else 1 + power(x >> 1)
        a = [(power(x), x) for x in range(lo, hi + 1)]
        a.sort()
        print(a)
        return a[k - 1][1]
