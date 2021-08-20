from collections import defaultdict as dt


class Solution:

    def getProbability(self, balls: List[int]) -> float:
        self.total = self.valid = 0
        fact = [1] * 50
        for i in range(1, len(fact)):
            fact[i] = fact[i - 1] * i

        def run(b1, b2, c1, c2, p1, p2, idx, n):
            if b1 > n / 2 or b2 > n / 2:
                return
            if idx == len(balls):
                times = fact[b1] / p1 * fact[b2] / p2
                self.total += times
                self.valid += times * int(c1 == c2)
            else:
                for x in range(balls[idx] + 1):
                    run(b1 + x, b2 + (balls[idx] - x), c1 + int(x > 0), c2 + int(balls[idx] - x > 0), p1 * fact[x], p2 * fact[balls[idx] - x], idx + 1, n)
        run(0, 0, 0, 0, 1.0, 1.0, 0, sum(balls))
        return self.valid / self.total
