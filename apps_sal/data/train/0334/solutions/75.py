class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        ans, n, prev = 0, len(s), 0
        for i in range(1, n):
            if s[i] == s[i - 1]:
                if cost[i] > cost[prev]:
                    ans += cost[prev]
                    prev = i
                else: ans += cost[i]
            else: prev = i
        return ans

