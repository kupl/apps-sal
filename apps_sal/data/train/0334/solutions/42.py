class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        c = 0
        p = 0
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                p = i
                continue

            if cost[p] > cost[i]:
                c += cost[i]
            else:
                c += cost[p]
                p = i

        return c
