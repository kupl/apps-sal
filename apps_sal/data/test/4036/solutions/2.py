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
        k = self.next_int()
        rs = []
        low = 1
        high = n + 1
        for i in range(0, k):
            kk = k - i
            high1 = high
            low1 = low
            while high1 - low1 > 1:
                mid = (low1 + high1) // 2
                if self.test_low(mid, n, kk):
                    low1 = mid
                else:
                    high1 = mid
            high2 = high
            low2 = low1
            while high2 - low2 > 1:
                mid = (low2 + high2) // 2
                if self.test_high(mid, n, kk):
                    low2 = mid
                else:
                    high2 = mid

            if not self.test_low(low1, n, kk) or not self.test_high(low2, n, kk):
                print('NO')
                return
            rs.append(low1)
            low = rs[-1] + 1
            high = rs[-1] * 2 + 1
            n -= rs[-1]
        print('YES')
        print(' '.join([str(x) for x in rs]))

    def test_low(self, d, n, k):
        return (2 * d + k - 1) * k // 2 <= n

    def test_high(self, d, n, k):
        return k >= 33 or (2 ** k - 1) * d >= n


def __starting_point():
    Main().solve()


__starting_point()
