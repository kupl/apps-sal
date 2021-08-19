class Solution:

    def minCost(self, s: str, cost: List[int]) -> int:
        res = 0
        i = 0
        while i < len(s) - 1:
            temp = i
            while i < len(s) - 1 and s[i] == s[i + 1]:
                i += 1
            if temp < i:
                res += sum(cost[temp:i + 1]) - max(cost[temp:i + 1])
            i += 1
        return res
