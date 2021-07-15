# AC
import sys


class Main:
    def __init__(self):
        self.buff = None
        self.index = 0

    def __next__(self):
        if self.buff is None or self.index == len(self.buff):
            self.buff = self.next_line()
            self.index = 0
        val = self.buff[self.index]
        self.index += 1
        return val

    def next_line(self):
        return sys.stdin.readline().split()

    def next_ints(self):
        return [int(x) for x in sys.stdin.readline().split()]

    def next_int(self):
        return int(next(self))

    def solve(self):
        n = self.next_int()
        x = sorted(self.next_ints())
        res = 0
        for _x in x:
            if _x > res:
                res += 1
        print(res)


def __starting_point():
    Main().solve()

__starting_point()
