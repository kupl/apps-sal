class Solution:

    def minCost(self, s: str, cost: List[int]) -> int:
        i = 0
        j = 1
        p = 0
        while j < len(s):
            if s[i] == s[j]:
                if cost[i] < cost[j]:
                    p += cost[i]
                    i = j
                    j += 1
                else:
                    p += cost[j]
                    j += 1
            else:
                i = j
                j += 1
        return p
