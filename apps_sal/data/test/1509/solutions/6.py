# AC
import sys


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
        x = [self.next_int() for _ in range(0, n)]
        ans = 0
        for i in range(0, n):
            ans += x[i] * (n - x[i] + 1)
            if i > 0:
                ans -= min(x[i], x[i - 1]) * (n - max(x[i], x[i - 1]) + 1)
        print(ans)


def __starting_point():
    Main().solve()


__starting_point()
