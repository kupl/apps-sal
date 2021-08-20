class Solution:

    def minCost(self, s: str, cost) -> int:
        l = 0
        ans = 0
        while l < len(s):
            r = l + 1
            if r < len(s) and s[r] == s[l]:
                tmp_cost = cost[l]
                max_cost = cost[l]
                while r < len(s) and s[r] == s[l]:
                    max_cost = max(max_cost, cost[r])
                    tmp_cost += cost[r]
                    r += 1
                ans += tmp_cost - max_cost
            l = r
        return ans
