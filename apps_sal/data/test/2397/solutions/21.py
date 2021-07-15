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
        n, k = self.next_ints()
        x = self.next_ints()
        ss = []
        s = 0
        for a in x[::-1]:
            s += a
            ss.append(s)
        ss = sorted(ss[:-1], reverse=True)
        print(s + sum(ss[:k - 1]))


def __starting_point():
    Main().solve()

__starting_point()
