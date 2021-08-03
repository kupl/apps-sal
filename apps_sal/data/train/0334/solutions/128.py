class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:

        i = 0
        tot = 0
        while i < len(s) - 1:
            if s[i] == s[i + 1]:
                start = i
                while i < len(s) - 1 and s[i] == s[i + 1]:
                    i += 1
                mx = 0
                for c in cost[start: i + 1]:
                    tot += c
                    mx = max(mx, c)
                tot -= mx
            i += 1
        return tot
