class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        # dp[color][blocks]

        dp, dp2 = {(0, 0): 0}, {}

        for index, house in enumerate(houses):
            for cj in (range(1, n + 1) if house == 0 else [house]):
                for ci, b in dp:
                    b2 = b + (ci != cj)
                    if b2 > target:
                        continue
                    dp2[cj, b2] = min(dp2.get((cj, b2), float('inf')), dp[ci, b] + (cost[index][cj - 1] if cj != house else 0))
            dp, dp2 = dp2, {}
        return min([dp[c, b] for c, b in dp if b == target] or [-1])
