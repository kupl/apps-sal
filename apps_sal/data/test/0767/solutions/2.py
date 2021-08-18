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
        z = self.next_int()
        x = sorted([self.next_int() for _ in range(0, n)])
        low = 0
        high = n
        while high - low > 1:
            mid = (low + high) // 2
            if self.test(mid, n, x, z):
                low = mid
            else:
                high = mid
        print(low)

    def test(self, mid, n, x, z):
        j = mid
        for i in range(0, mid):
            while j < n and x[j] < x[i] + z:
                j += 1
            if j >= n:
                return False
            j += 1
        return True


def __starting_point():
    Main().solve()


__starting_point()
