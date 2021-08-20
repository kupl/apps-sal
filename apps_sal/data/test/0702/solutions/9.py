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
        ss = [[s for s in next(self)] for _ in range(0, n)]
        for i in range(0, n):
            for j in range(0, n):
                if ss[i][j] == '.':
                    if j == 0 or j == n - 1 or i >= n - 2:
                        print('NO')
                        return
                    if ss[i + 1][j - 1] != '.' or ss[i + 1][j] != '.' or ss[i + 1][j + 1] != '.' or (ss[i + 2][j] != '.'):
                        print('NO')
                        return
                    ss[i + 1][j - 1] = '#'
                    ss[i + 1][j] = '#'
                    ss[i + 1][j + 1] = '#'
                    ss[i + 2][j] = '#'
        print('YES')


def __starting_point():
    Main().solve()


__starting_point()
