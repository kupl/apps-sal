class Solution:

    def minCost(self, s: str, cost: List[int]) -> int:
        rep = []
        p1 = 0
        p2 = 1
        n = len(s)
        if n == 1:
            return 0
        while p1 < n and p2 < n:
            if s[p1] == s[p2]:
                p2 += 1
            elif p2 - p1 > 1:
                rep.append((p1, p2 - 1))
                p1 = p2
                p2 = p1 + 1
            else:
                p1 += 1
                p2 += 1
        if p1 != n - 1:
            rep.append((p1, p2 - 1))
        ans = 0
        for r in rep:
            (a, b) = r
            big = float('-inf')
            minus = 0
            for i in range(a, b + 1):
                big = max(big, cost[i])
                minus += cost[i]
            ans += minus - big
        return ans
