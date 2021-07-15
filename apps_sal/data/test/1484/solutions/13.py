# AC
import sys
from heapq import heappush, heappop


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

    def pp(self, a, b, mod):
        if b == 0:
            return 1
        tmp = self.pp(a, b // 2, mod)
        tmp = tmp * tmp % mod
        if b % 2 == 1:
            tmp = tmp * a % mod
        return tmp

    def same(self, cc, k, mod):
        t = 1
        y = 0
        for i in range(0, cc):
            tt = y
            yy = (t * (k - 1) + y * (k - 2)) % mod
            y = yy
            t = tt
        return y

    def diff(self, cc, k, mod):
        t = 0
        y = 1
        for i in range(0, cc):
            tt = y
            yy = (t * (k - 1) + y * (k - 2)) % mod
            y = yy
            t = tt
        return y

    def solve(self):
        n = self.next_int()
        k = self.next_int()
        mod = 998244353
        pre = [-1, -1]
        cc = [0, 0]
        ans = 1
        for i in range(0, n):
            d = self.next_int()
            ii = i % 2
            if d == -1:
                cc[ii] += 1
            else:
                if pre[ii] == -1:
                    ans = ans * self.pp(k - 1, cc[ii], mod) % mod
                elif pre[ii] == d:
                    ans = ans * self.same(cc[ii], k, mod) % mod
                else:
                    ans = ans * self.diff(cc[ii], k, mod) % mod
                cc[ii] = 0
                pre[ii] = d
        if cc[0] == (n + 1) // 2:
            ans = ans * k * self.pp(k - 1, cc[0] - 1, mod) % mod
        else:
            ans = ans * self.pp(k - 1, cc[0], mod) % mod
        if cc[1] == n // 2:
            ans = ans * k * self.pp(k - 1, cc[1] - 1, mod) % mod
        else:
            ans = ans * self.pp(k - 1, cc[1], mod) % mod
        print(ans)


def __starting_point():
    Main().solve()

__starting_point()
