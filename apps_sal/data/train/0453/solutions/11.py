# k: num of neighborhoods, i: num of houses, c: color of the last house
# dp[k][i][c]: min cost to form k neighborhoods using the first i houses and the i-th house's color is c
# init: dp[0][0][*] = 0, else is inf
# if the i - 1 house's color != i house's color, means they are not in the same neighborhood
# dp[k][i][ci] = dp[k - 1][i - 1][ci-1] + cost
# else if the i - 1house's color == i house's color, means they are in the same neighborhood
# dp[k][i][ci] = dp[k][i - 1][ci-1] + cost
# if houses[i] == ci, house i is painted by color i, cost = 0, no need to paint
# else, cost = cost[i][ci]
# if ci != houses[i], means house i is painted by another color, dp[k][i][ci] = inf
# ans = min(dp[target][m][*])
# 因为需要枚举所有的 house i - 1 和 house i 的颜色的组合, 所以时间复杂度乘以 n * n
# 因为 dp[k] 只和 dp[k] 和 dp[k - 1] 有关, 所以时间复杂度可以从 O(target * m * n) -> O(m * n)
# O(target * m * n * n) time compleixty, O(m * n) space complexity
class Solution:
    def minCost(self, houses: List[int], costs: List[List[int]], m: int, n: int, target: int) -> int:
        dp = [[[float('inf') for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(target + 1)]
        for c in range(n + 1):
            dp[0][0][c] = 0

        for k in range(1, target + 1):
            for i in range(k, m + 1):  # 因为 i < k 的情况不合法, 组成 k 个 neighborhoods 至少也需要 k 个 house
                hi = houses[i - 1]
                hj = 0  # 初始化前一个房子的颜色为 0, 如果 i < 2, 则它就是第一个房子, 所以设前一个房子可以是任何颜色的, 即 0
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
