from typing import List


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
            c_overall = self.combination(spaceA + spaceB, currentBallCount)
            for i in range(max(currentBallCount - spaceB, 0), min(currentBallCount, spaceA) + 1):
                j = currentBallCount - i
                c1 = self.combination(spaceA, i)
                c2 = self.combination(spaceB, j)
                p = c1 * c2 / c_overall
                dfs(spaceA=spaceA - i, spaceB=spaceB - j, colorsA=colorsA + (i != 0), colorsB=colorsB + (j != 0), remainBalls=remainBalls[1:], probability=probability * p)
        dfs(spaceA=total // 2, spaceB=total // 2, colorsA=0, colorsB=0, remainBalls=balls, probability=1)
        return result


s = Solution()
print(s.getProbability([1, 1]))
print(s.getProbability([2, 1, 1]))
print(s.getProbability([1, 2, 1, 2]))
print(s.getProbability([6, 6, 6, 6, 6, 6]))
