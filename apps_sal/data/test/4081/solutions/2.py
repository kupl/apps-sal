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
        d = 0
        l = 0
        r = n - 1
        rs = []
        while l <= r:
            if x[l] < d and x[r] < d:
                break
            if x[l] < d:
                rs.append('R')
                d = x[r]
                r -= 1
            elif x[r] < d:
                rs.append('L')
                d = x[l]
                l += 1
            elif x[r] < x[l]:
                rs.append('R')
                d = x[r]
                r -= 1
            else:
                rs.append('L')
                d = x[l]
                l += 1
        print(len(rs))
        print(''.join(rs))


def __starting_point():
    Main().solve()


__starting_point()
