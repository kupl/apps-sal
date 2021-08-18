class Solution:
    def minCost(self, houses: List[int], costs: List[List[int]], m: int, n: int, target: int) -> int:
        dp = [[[float('inf') for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(target + 1)]
        for c in range(n + 1):
            dp[0][0][c] = 0

        for k in range(1, target + 1):
            for i in range(k, m + 1):
                hi = houses[i - 1]
                hj = 0
                if i >= 2:
                    hj = houses[i - 2]
                for ci in range(1, n + 1):
                    if hi != 0 and hi != ci:
                        dp[k][i][ci] = float('inf')
                        continue
                    cost = 0
                    if hi != ci:
                        cost = costs[i - 1][ci - 1]
                    for cj in range(1, n + 1):
                        dp[k][i][ci] = min(dp[k][i][ci], dp[k - (ci != cj)][i - 1][cj] + cost)

        res = min(dp[target][m][c] for c in range(1, n + 1))
        if res == float('inf'):
            return -1
        return res
