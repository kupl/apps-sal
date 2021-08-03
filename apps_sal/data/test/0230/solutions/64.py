class RollingHash():
    def __init__(self, s):
        self.n = n = len(s)
        self.b = b = 129
        self.M = M = 2**61 - 1
        x, y = 1, 0
        self.f = f = [x] * (n + 1)
        self.h = h = [y] * (n + 1)
        for i, c in enumerate(s.encode()):
            f[i + 1] = x = x * b % M
            h[i + 1] = y = (y * b + c) % M

    def get(self, l, r):
        return(self.h[r] - self.h[l] * self.f[r - l]) % self.M


def main():
    n = int(input())
    s = RollingHash(input())
    ok, ng = 0, n
    while ng - ok > 1:
        mid = ok + ng >> 1
        d = {}
        for i in range(0, n - mid + 1):
            k = s.get(i, i + mid)
            if k in d:
                if d[k] + mid <= i:
                    ok = mid
                    break
            else:
                d[k] = i
        else:
            ng = mid
    print(ok)


main()
