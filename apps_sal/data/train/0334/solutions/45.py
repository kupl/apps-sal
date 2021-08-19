class Solution:

    def minCost(self, s: str, cost: List[int]) -> int:
        n = len(cost)
        if n <= 1:
            return 0
        res = 0
        i = 1
        while i < n:
            if s[i] == s[i - 1]:
                j = i
                while j < n and s[j] == s[j - 1]:
                    j += 1
                res += sum(cost[i - 1:j]) - max(cost[i - 1:j])
                i = j
            else:
                i += 1
        return res
