# AC
import sys
from math import gcd


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
        pr = [(self.next_int(), self.next_int()) for _ in range(0, n)]
        ks = {}
        ct = 0
        res = 0
        ls = set()
        for i in range(0, n):
            for j in range(i + 1, n):
                dy = pr[j][1] - pr[i][1]
                dx = pr[j][0] - pr[i][0]
                if dx < 0:
                    dx *= -1
                    dy *= -1
                elif dx == 0:
                    dy = abs(dy)
                g = gcd(abs(dx), abs(dy))
                k = (dx // g, dy // g)
                x, y = pr[i][0], pr[i][1]
                if dx == 0:
                    a = (pr[i][0], 0)
                else:
                    cl = abs(x) // k[0]
                    if x >= 0:
                        x -= cl * k[0]
                        y -= cl * k[1]
                    else:
                        x += cl * k[0]
                        y += cl * k[1]
                        while x < 0:
                            x += k[0]
                            y += k[1]
                    a = (x, y)
                if (k, a) in ls:
                    continue
                else:
                    ls.add((k, a))
                ct += 1
                if k not in ks:
                    ks[k] = 1
                else:
                    ks[k] += 1
                res += ct - ks[k]
        print(res)


def __starting_point():
    Main().solve()


__starting_point()
