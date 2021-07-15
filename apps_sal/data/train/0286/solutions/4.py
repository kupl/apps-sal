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
        self.ball_sums = [sum(balls[index :]) for index in range(self.k + 1)]
        self.update([], 0, 0)
        return self.valid / self.total
    
    @ft.lru_cache(None)
    def factorial(self, n: int) -> int:
        return math.factorial(n)

    @ft.lru_cache(None)
    def count(self, *balls: int) -> int:
        return self.factorial(self.n) // ft.reduce(operator.mul, map(self.factorial, balls))
    
    def update(self, left_balls: List[int], total: int, delta: int) -> None:
        if len(left_balls) == self.k:
            if total != self.n:
                return
            right_balls = [total_cnt - left_cnt for left_cnt, total_cnt in zip(left_balls, self.balls)]
            count = self.count(*sorted(left_balls)) * self.count(*sorted(right_balls))
            self.total += count
            if delta == 0:
                self.valid += count
            return
        index = len(left_balls)
        if total + self.ball_sums[index] < self.n:
            return
        if total > self.n:
            return
        if index == self.k - 1:
            new_delta = delta + (self.n - total == self.balls[index]) - (self.n - total == 0)
            self.update(left_balls + [self.n - total], self.n, new_delta)
            return
        for cnt in range(self.balls[index] + 1):
            new_delta = delta + (cnt == self.balls[index]) - (cnt == 0)
            self.update(left_balls + [cnt], total + cnt, new_delta)
