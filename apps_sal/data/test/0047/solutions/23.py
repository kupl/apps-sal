# AC
import sys
from math import gcd


class Main:
    def __init__(self):
        self.buff = None
        self.index = 0

    def __next__(self):
        if self.buff is None or self.index == len(self.buff):
            self.buff = sys.stdin.readline().split()
            self.index = 0
        val = self.buff[self.index]
        self.index += 1
        return val

    def next_int(self):
        return int(next(self))

    def solve(self):
        n = self.next_int()
        k = self.next_int()
        x = [self.next_int() for _ in range(0, n)]
        ans = 0
        dp = (0, 0, 0)
        for xx in x:
            d0 = max(0, dp[0]) + xx
            d1 = max(0, dp[0], dp[1]) + xx * k
            d2 = max(0, dp[0], dp[1], dp[2]) + xx
            ans = max(ans, d0, d1, d2)
            dp = (d0, d1, d2)
        print(ans)


def __starting_point():
    Main().solve()


__starting_point()
