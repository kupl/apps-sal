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
        n = self.next_int()
        a = self.next_ints()
        b = sorted(self.next_ints())[::-1]
        for i in range(0, n):
            mm = (i + 1) * (n - i)
            a[i] *= mm
        a = sorted(a)
        mod = 998244353
        c = [a[i] * b[i] % mod for i in range(0, n)]
        print(sum(c) % mod)


def __starting_point():
    Main().solve()


__starting_point()
