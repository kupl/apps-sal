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
        s = [int(x) for x in next(self)]
        x = [self.next_int() for _ in range(0, 9)]
        id = 0
        while id < n and s[id] >= x[s[id] - 1]:
            id += 1
        while id < n and s[id] <= x[s[id] - 1]:
            s[id] = x[s[id] - 1]
            id += 1
        print(''.join([str(x) for x in s]))


def __starting_point():
    Main().solve()


__starting_point()
