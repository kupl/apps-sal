class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:

        if len(s) <= 1:
            return 0

        index = 1
        to_remove = 0

        while index < len(s):
            if s[index] != s[index - 1]:
                index += 1
                continue
            k = index
            while k < len(s) and s[k] == s[index - 1]:
                k += 1
            to_remove += (sum(cost[index - 1:k]) - max(cost[index - 1:k]))
            index = k

        return to_remove
