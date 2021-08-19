import sys


def unique(lst):
    return list(dict(((o, o) for o in lst)).values())


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
        x = [self.next_int() for _ in range(0, n)]
        r = 0
        for i in range(1, n):
            if x[i - 1] == 1:
                if x[i] == 2:
                    if i >= 2 and x[i - 2] == 3:
                        r += 2
                    else:
                        r += 3
                elif x[i] == 3:
                    r += 4
            elif x[i - 1] == 2:
                if x[i] == 1:
                    r += 3
                elif x[i] == 3:
                    r = -1
                    break
            elif x[i - 1] == 3:
                if x[i] == 1:
                    r += 4
                elif x[i] == 2:
                    r = -1
                    break
        if r == -1:
            print('Infinite')
        else:
            print('Finite')
            print(r)


def __starting_point():
    Main().solve()


__starting_point()
