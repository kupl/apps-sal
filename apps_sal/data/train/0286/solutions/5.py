import math


class Solution:

    def Prob(self, balls: List[int], left: int, right: int, diff: int) -> float:
        if len(balls) == 1:
            return 1 if left * right != 0 and diff == 0 or (left == 0 and diff == -1) or (right == 0 and diff == 1) else 0
        a = balls[-1]
        p = [float(math.comb(a, i) * math.prod(range(left - i + 1, left + 1)) * math.prod(range(right - a + i + 1, right + 1))) / math.prod(range(left + right - a + 1, left + right + 1)) for i in range(a + 1)]
        A = [self.Prob(balls[:-1], left, right - a, diff + 1)] + [self.Prob(balls[:-1], left - i, right - a + i, diff) for i in range(1, a)] + [self.Prob(balls[:-1], left - a, right, diff - 1)]
        S = sum((p[i] * A[i] for i in range(a + 1)))
        return S

    def getProbability(self, balls: List[int]) -> float:
        return self.Prob(balls, sum(balls) // 2, sum(balls) // 2, 0)
