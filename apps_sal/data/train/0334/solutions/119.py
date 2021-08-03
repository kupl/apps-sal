class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:

        @lru_cache
        def f(s, i):
            if i == len(s):
                return 0
            j = i
            while j + 1 < len(s) and s[j] == s[j + 1]:
                j += 1

            if j == i:
                a = 0
            else:
                xx = sorted([cost[k] for k in range(i, j + 1)])
                a = sum(xx[:-1])

            return a + f(s, j + 1)

        return f(s, 0)
