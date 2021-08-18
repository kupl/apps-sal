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

    def next_line(self, _map=str):
        return list(map(_map, sys.stdin.readline().split()))

    def next_int(self):
        return int(next(self))

    def solve(self):
        n = self.next_int()
        rs = {}
        while n not in rs:
            rs[n] = n
            n += 1
            while n % 10 == 0:
                n /= 10
        print(len(rs))


def __starting_point():
    Main().solve()


__starting_point()
