cache = {1: 0}


class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:

        def get_power(x, count=0):
            if x in cache:
                return cache[x] + count
            return get_power(x * 3 + 1 if x & 1 else x // 2, count + 1)
        cache.update({i: get_power(i) for i in range(lo, hi + 1) if i not in cache})
        return sorted((x for x in list(cache.items()) if lo <= x[0] <= hi), key=lambda x: x[1])[k - 1][0]
