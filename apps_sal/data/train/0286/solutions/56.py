import functools as ft
import math
import operator


class Solution:

    def getProbability(self, balls: List[int]) -> float:
        self.total = 0
        self.valid = 0
        self.balls = balls
        self.k = len(balls)
        self.n = sum(balls) // 2
        self.update([])
        return self.valid / self.total

    @ft.lru_cache(None)
    def combination(self, n: int, p: int) -> int:
        return ft.reduce(operator.mul, range(n, n - p, -1), 1) // math.factorial(p)

    def count(self, balls: List[int]) -> int:
        ans = 1
        remaining = self.n
        for ball in balls:
            ans *= self.combination(remaining, ball)
            remaining -= ball
        return ans

    def update(self, left_balls: List[int]) -> None:
        if len(left_balls) == self.k:
            if sum(left_balls) != self.n:
                return
            right_balls = [total_cnt - left_cnt for (left_cnt, total_cnt) in zip(left_balls, self.balls)]
            count = self.count(left_balls) * self.count(right_balls)
            self.total += count
            if sum((left_cnt == 0 for left_cnt in left_balls)) == sum((right_cnt == 0 for right_cnt in right_balls)):
                self.valid += count
            return
        index = len(left_balls)
        left_total = sum(left_balls)
        if left_total + sum(self.balls[index:]) < self.n:
            return
        if left_total > self.n:
            return
        for cnt in range(self.balls[index] + 1):
            self.update(left_balls + [cnt])
