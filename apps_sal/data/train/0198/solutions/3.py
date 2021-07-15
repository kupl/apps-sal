class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        if not s: return 0
        costs = [abs(ord(si)-ord(ti)) for si, ti in zip(s, t)]
        ans = 0
        l, r = 0, 0
        cur_cost = 0
        print(costs)
        while l < len(s) and r < len(s):
            while r < len(s) and cur_cost <= maxCost:
                cur_cost += costs[r]
                r += 1
            ans = max(ans, r-l-1)
            
            while l < r and cur_cost > maxCost:
                cur_cost -= costs[l]
                l += 1
        ans = max(ans, r-l)
        return ans
        

