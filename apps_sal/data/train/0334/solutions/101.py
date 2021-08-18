from functools import reduce


class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        t = 0
        n = len(s)
        if n <= 1:
            return 0
        ins = s
        s = n
        p = '?'
        e = -1
        for i, l in enumerate(ins):
            if p == l:
                if s == n:
                    s = i - 1
            else:
                p = l
                if s != n:
                    t += reduce(lambda a, b: a + b, cost[s:i], 0) - max(cost[s:i])
                    s = n
        if s != n:
            t += reduce(lambda a, b: a + b, cost[s:], 0) - max(cost[s:])
        return t
