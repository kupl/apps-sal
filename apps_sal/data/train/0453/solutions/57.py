from collections import defaultdict


class Solution:

    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        """

        m houses - n colors (1~n)
        neighborhoods of same color
        0 = not colored yet
        cost[i][j] - cost to paint i with color j+1

        return minimal cost of painting remaining houses to get exactly target neighborhoods

        -have to keep track of min cost
        -num neighbors==target at end

        dp => cost,numNeighbors
        dp[house][lastneighbor] = min(dp[house][lastneighbor], min(cost + dp[house-1][neighbors])

        best now = last house with same color, correct num of neighbors or last house diff color, 1 less num of neighbors

        dp[h][numNeighbors][color] = colorCost + min(
                dp[h-1][numNeighbors][color],
                dp[h-1][numNeighbors-1][diffColor] <- iterate
            )

        at house h,
        dp[neighbors][color] = colorCost (if it's 0)
                                + prev[neighbors][color]
                                + prev[neighbors-1][anothercolor]
        neighbors: [j-target,j+1]

        edge cases:
        -if # of color neighborhoods > target: return -1
        -num houses < target: return -1
        """
        prev = [[0] * n for _ in range(2)]
        for (h, house) in enumerate(houses):
            dp = [[float('inf')] * n for _ in range(h + 2)]
            for numNeighbors in range(1, h + 2):
                if house == 0:
                    for color in range(n):
                        colorCost = cost[h][color]
                        if numNeighbors == h + 1:
                            dp[numNeighbors][color] = min(dp[numNeighbors][color], colorCost + min((prev[numNeighbors - 1][c] for c in range(n) if c != color)))
                        else:
                            dp[numNeighbors][color] = min(dp[numNeighbors][color], colorCost + prev[numNeighbors][color], colorCost + min((prev[numNeighbors - 1][c] for c in range(n) if c != color)))
                else:
                    color = house - 1
                    if numNeighbors == h + 1:
                        dp[numNeighbors][color] = min(dp[numNeighbors][color], min((prev[numNeighbors - 1][c] for c in range(n) if c != color)))
                    else:
                        dp[numNeighbors][color] = min(dp[numNeighbors][color], prev[numNeighbors][color], min((prev[numNeighbors - 1][c] for c in range(n) if c != color)))
            prev = dp
        out = min((prev[target][c] for c in range(n)))
        return out if out != float('inf') else -1
