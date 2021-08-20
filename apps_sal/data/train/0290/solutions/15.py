class Solution:

    def minCost(self, n: int, cuts: List[int]) -> int:
        cache = dict()

        def recurse(start, end):
            key = (start, end)
            if key in cache:
                return cache[key]
            if start >= end:
                return 0
            minCost = float('inf')
            len = end - start
            for cut in cuts:
                if cut > start and cut < end:
                    first = recurse(start, cut)
                    second = recurse(cut, end)
                    minCost = min(minCost, len + first + second)
            if minCost == float('inf'):
                minCost = 0
            cache[key] = minCost
            return minCost
        cuts.sort()
        ans = recurse(0, n)
        return ans
