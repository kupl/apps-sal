class Solution:

    def minCost(self, s: str, cost: List[int]) -> int:
        s += '~'

        def dedup(exp: List[int]):
            return sum(exp) - max(exp)
        res = 0
        i = 0
        current = []
        while i + 1 < len(s):
            if s[i + 1] == s[i]:
                if len(current) == 0:
                    current.append(cost[i])
                current.append(cost[i + 1])
            if s[i + 1] != s[i]:
                if len(current) > 1:
                    res += dedup(current)
                current = []
            i += 1
        return res
