class Solution:

    def minCost(self, s: str, cost: List[int]) -> int:
        res = 0
        (i, n) = (0, len(s))
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            if j != i + 1:
                res += sum(cost[i:j]) - max(cost[i:j])
            i = j
        return res
