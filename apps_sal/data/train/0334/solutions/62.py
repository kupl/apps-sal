class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        res = 0
        if len(s) < 2: return res
        first, second = 0, 1
        while second < len(s):
            if s[first] == s[second]:
                if cost[first] <= cost[second]:
                    res += cost[first]
                    first = second
                    second += 1
                else:
                    res += cost[second]
                    second += 1
            else:
                first = second
                second += 1
        return res

