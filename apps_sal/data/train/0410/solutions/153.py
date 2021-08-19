class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:
        cache = {1: 0}

        def power(n):
            if n in cache:
                return cache[n]
            if n & 1:
                cache[n] = 1 + power(3 * n + 1)
                return cache[n]
            else:
                cache[n] = 1 + power(n // 2)
                return cache[n]
        out = []
        for i in range(lo, hi + 1):
            out.append([i, power(i)])
        out.sort(key=lambda x: x[1])
        return out[k - 1][0]
