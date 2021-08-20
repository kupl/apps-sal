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
        k = self.next_int()
        x = [self.next_int() for _ in range(0, n)]
        bf = [x - 1 for x in range(0, n)]
        nx = [x + 1 for x in range(0, n)]
        t = [0 for _ in range(0, n)]
        od = [0 for _ in range(0, n)]
        for i in range(0, n):
            od[x[i] - 1] = i
        tt = 1
        for i in range(n - 1, -1, -1):
            if t[od[i]] == 0:
                o = od[i]
                t[o] = tt
                for _ in range(0, k):
                    o = bf[o]
                    if o == -1:
                        break
                    t[o] = tt
                oo = od[i]
                for _ in range(0, k):
                    oo = nx[oo]
                    if oo == n:
                        break
                    t[oo] = tt
                if o != -1 and bf[o] != -1:
                    nx[bf[o]] = oo if oo == n else nx[oo]
                if oo != n and nx[oo] != n:
                    bf[nx[oo]] = o if o == -1 else bf[o]
                tt = 3 - tt
        print(''.join([str(xx) for xx in t]))


def __starting_point():
    Main().solve()


__starting_point()
