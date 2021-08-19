class Solution:

    def superEggDrop(self, K: int, N: int) -> int:
        INF = N + 1
        cache = {}

        def eggDropHelper(k, n):
            if (k, n) in cache:
                return cache[k, n]
            if k < 0:
                return INF
            if n == 0:
                return 0
            if k == 0:
                return INF
            optAns = INF
            (l, r) = (1, n)
            while l + 1 < r:
                m = (l + r) // 2
                (left, right) = (eggDropHelper(k - 1, m - 1), eggDropHelper(k, n - m))
                if left < right:
                    l = m
                elif left > right:
                    r = m
                else:
                    l = r = m
                    break
            optAns = max(eggDropHelper(k - 1, l - 1), eggDropHelper(k, n - l)) + 1
            currAns = max(eggDropHelper(k - 1, r - 1), eggDropHelper(k, n - r)) + 1
            optAns = min(currAns, optAns)
            cache[k, n] = optAns
            return cache[k, n]
        return eggDropHelper(K, N)
