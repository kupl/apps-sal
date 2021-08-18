class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        def dps():

            def remove_from_first(T, s):
                assert(len(s) == 3)
                L = list(T)
                for x in s:
                    if x in L:
                        L.remove(x)
                return tuple(L)

            from itertools import combinations
            from functools import lru_cache

            @lru_cache(None)
            def dp(T):
                if len(T) == 0:
                    return 0
                if len(T) == 3:
                    return sum(T) - max(T) - min(T)

                mxl = 0
                for cm in combinations(T, 3):
                    S = remove_from_first(T, cm)
                    mxl = max(mxl, dp(S) + sum(cm) - max(cm) - min(cm))
                return mxl

            return dp(tuple(piles))

        def iter_appr():
            assert(len(piles) % 3 == 0)
            maxheap, minheap = [], []
            counter = 0
            from heapq import heappush, heappop
            for x in piles:
                heappush(maxheap, -x)
                heappush(minheap, x)

            alice, me, bob = 0, 0, 0
            while maxheap and minheap and counter < len(piles):
                alice += -heappop(maxheap)
                me += -heappop(maxheap)
                bob += heappop(minheap)
                counter += 3
            return me
        return iter_appr()
