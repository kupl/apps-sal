class Solution:

    def minCost(self, s: str, cost: List[int]) -> int:
        ans = 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                ans += min(cost[i], cost[i - 1])
                cost[i] = max(cost[i], cost[i - 1])
        return ans
