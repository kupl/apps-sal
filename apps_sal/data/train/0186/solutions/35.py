from functools import lru_cache


class Solution:
    @lru_cache(None)
    def recursive(self, k):
        if k == 0:
            return ''
        ans = []
        for x in self.d:
            if x <= k:
                r = self.recursive(k - x)
                if r != '0':
                    ans.append(self.d[x] + r)
        return str(max(map(int, ans))) if ans else '0'

    def largestNumber(self, cost: List[int], target: int) -> str:
        self.d = {}
        for i, x in enumerate(cost):
            self.d[x] = str(i + 1)
        self.recursive.cache_clear()
        return self.recursive(target)
