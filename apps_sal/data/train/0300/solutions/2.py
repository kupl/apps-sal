from functools import lru_cache


class Solution:

    def leastOpsExpressTarget(self, x: int, target: int) -> int:

        @lru_cache(None)
        def search(t: int) -> int:
            if x == t:
                return 0
            if t < x:
                (d1, d2) = (t, x - t)
                return min(2 * d1 - 1, 2 * d2)
            k1 = int(math.log(t, x))
            y1 = x ** k1
            if y1 == t:
                return k1 - 1
            total = k1 + search(t - y1)
            k2 = k1 + 1
            y2 = x ** k2
            if y2 <= 2 * t - y1:
                total = min(total, k2 + search(y2 - t))
            return total
        return search(target)
