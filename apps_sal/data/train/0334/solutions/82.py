class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        n = len(s)
        res = 0
        i = j = 0
        while j < n:
            i = j
            while j + 1 < n and s[j] == s[j + 1]:
                j += 1
            res += sum(cost[i:j + 1]) - max(cost[i:j + 1] or [0])
            j += 1
        return res
