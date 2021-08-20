class Solution:

    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        dp = {(0, 0): 0}
        dp2 = {}
        for (index, house) in enumerate(houses):
            for color in list(range(1, n + 1)) if house == 0 else [house]:
                for (preColor, block) in dp:
                    newBlock = 0
                    if preColor == color:
                        newBlock = block
                    else:
                        newBlock = block + 1
                    if newBlock > target:
                        continue
                    dp2[color, newBlock] = min(dp2.get((color, newBlock), float('inf')), dp[preColor, block] + (cost[index][color - 1] if color != house else 0))
            (dp, dp2) = (dp2, {})
            print(dp)
        return min([dp[i, color] for (i, color) in dp if color == target] or [-1])
