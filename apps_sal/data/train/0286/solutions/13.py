from typing import List


# May 30 - May 31, 2002
# Reviewed: Sep 9, 2020. This is a math + dfs problem.
class Solution:
    def combination(self, N, K) -> int:
        res = 1
        for i in range(N, max(K, N - K), -1):
            res *= i
        for i in range(2, min(K, N - K) + 1):
            res /= i
        return res

    def getProbability(self, balls: List[int]) -> float:
        total = sum(balls)
        result = 0

        def dfs(spaceA: int, spaceB: int, colorsA: int, colorsB: int, remainBalls: List[int], probability: float):
            nonlocal result
            if not remainBalls:
                if colorsA == colorsB:
                    result += probability
                return

            currentBallCount = remainBalls[0]

            # The total number of ways to distribute the balls in the the boxes
            c_overall = self.combination(spaceA + spaceB, currentBallCount)

            # For the `currentBallCount`, assume i of them goes to box A and the rest goes to box B.
            # We need:
            # 1) `currentBallCount - i` to be within range of [0, spaceB], which give,
            #
            #     0 <= currentBallCount - i <= spaceB
            #     currentBallCount - spaceB <= i <= currentBallCount
            #
            # 2) i to be within range [0, spaceA]
            #
            # The overall range is [max(currentBallCount - spaceB), min(currentBallCount, spaceA)].
            for i in range(max(currentBallCount - spaceB, 0), min(currentBallCount, spaceA) + 1):
                j = currentBallCount - i

                # count the number of ways for i ball to go into box A and j balls to go into box B
                c1 = self.combination(spaceA, i)
                c2 = self.combination(spaceB, j)

                p = c1 * c2 / c_overall

                dfs(
                    spaceA=spaceA - i,
                    spaceB=spaceB - j,
                    colorsA=colorsA + (i != 0),
                    colorsB=colorsB + (j != 0),
                    remainBalls=remainBalls[1:],
                    probability=probability * p
                )

        dfs(spaceA=total // 2, spaceB=total // 2, colorsA=0, colorsB=0, remainBalls=balls, probability=1)
        return result


s = Solution()
print((s.getProbability([1, 1])))  # 1.0
print((s.getProbability([2, 1, 1])))  # 0.666666666
print((s.getProbability([1, 2, 1, 2])))  # 0.6
print((s.getProbability([6, 6, 6, 6, 6, 6])))  # 0.90327
