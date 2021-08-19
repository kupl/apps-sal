class Solution:

    def minCost(self, s: str, cost: List[int]) -> int:
        n = len(s)
        memo = {}

        def f(prev, i):
            if i == n:
                return 0
            if (prev, i) in memo:
                return memo[prev, i]
            if s[i] == prev:
                memo[prev, i] = cost[i] + f(s[i], i + 1)
            elif i + 1 >= n or s[i] != s[i + 1]:
                memo[prev, i] = f(s[i], i + 1)
            else:
                memo[prev, i] = min(cost[i] + f(prev, i + 1), f(s[i], i + 1))
            return memo[prev, i]
        return f(None, 0)
