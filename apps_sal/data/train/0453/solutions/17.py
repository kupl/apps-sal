class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        # dp[color][target]
        dp = {(0, 0): 0}
        for i in range(len(houses)):
            tmp = {}
            color = range(1, n + 1) if houses[i] == 0 else [houses[i]]
            for curr in color:
                for prev, j in dp:
                    t = j if curr == prev else j + 1
                    if t > target:
                        continue
                    tmp[curr, t] = min(tmp.get((curr, t), float('inf')), dp[prev, j] + (cost[i][curr - 1] if curr != houses[i] else 0))
            dp = tmp
        return min([dp[c, b] for c, b in dp if b == target] or [-1])
