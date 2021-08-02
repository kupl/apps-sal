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

    def cal(self, s):
        if len(s) == 1:
            return s[0]
        if s[0] == 0:
            return self.cal(s[1:])
        v = 1
        for c in s:
            v *= c
        return v

    def solve(self):
        n = self.next_int()
        m = self.next_int()
        h = self.next_int()
        f = [self.next_int() for _ in range(0, m)]
        l = [self.next_int() for _ in range(0, n)]
        for i in range(0, n):
            rs = []
            for j in range(0, m):
                if self.next_int() == 0:
                    rs.append(0)
                else:
                    rs.append(min(f[j], l[i]))
            print(' '.join([str(x) for x in rs]))


def __starting_point():
    Main().solve()


__starting_point()
