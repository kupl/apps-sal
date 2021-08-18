class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        if len(s) < 2:
            return 0
        i = 0
        ans = []
        while i < len(s) - 1:
            if s[i] == s[i + 1]:
                su = 0
                m = -1
                inside = False
                while i < len(s) - 1 and s[i] == s[i + 1]:
                    m = max(m, cost[i], cost[i + 1])
                    print((s[i], cost[i], s[i + 1], cost[i + 1]))
                    su += cost[i]
                    i += 1
                    inside = True
                if inside:
                    su += cost[i]
                    ans.append(su - m)
                i += 1

            else:
                i += 1
        return sum(ans)
