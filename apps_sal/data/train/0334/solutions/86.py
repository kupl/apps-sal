class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        ma, res, total = 0, 0, 0
        i = 0
        while i < len(s) - 1:
            start = i
            while i < len(s) - 1 and s[i + 1] == s[i]:
                i += 1
            end = i
            if start == end:
                i += 1
            else:
                for j in range(start, end + 1):
                    ma = max(ma, cost[j])
                    total += cost[j]
                res += total - ma
                ma = 0
                total = 0
        return res
