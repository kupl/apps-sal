class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        c = 0
        si = 0
        x = 1
        while x < len(s):
            if s[si] == s[x] and si < x:
                if cost[si] <= cost[x]:
                    c += cost[si]
                    si = x
                else:
                    c += cost[x]
            else:
                si = x
            x += 1
        return c
