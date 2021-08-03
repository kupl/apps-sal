from collections import defaultdict


class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        i = j = 0
        ans = 0
        while j < len(s):
            while j < len(s) and s[i] == s[j]:
                j += 1
            if j - i > 1:
                ans += sum(sorted(cost[i:j])[:-1])
            i = j

        return ans
