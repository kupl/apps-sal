class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        pre = 0
        res = 0
        for idx in range(1, len(s)):
            if s[idx] == s[pre]:
                res += min(cost[idx], cost[pre])
                print((cost[pre], cost[idx]))
            
            if s[idx] != s[pre] or cost[pre] < cost[idx]:
                pre = idx
        return res

