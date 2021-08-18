import sys
BASE, MOD1, MOD2 = (1 << 30), (1 << 61) - 1, (1 << 31) - 1


class RollingHash():
    def __init__(self, s, base, mod):
        self.mod = mod
        self.pw = pw = [1] * (len(s) + 1)

        l = len(s)
        self.h = h = [0] * (l + 1)

        v = 0
        for i in range(l):
            h[i + 1] = v = (v * base + s[i]) % mod
        v = 1
        for i in range(l):
            pw[i + 1] = v = v * base % mod

    # [l. r)
    def get(self, l, r):
        return (self.h[r] - self.h[l] * self.pw[r - l]) % self.mod

    def concatenate(self, l1, r1, l2, r2):
        return (self.get(l1, r1) * self.pw[r2 - l2] + self.get(l2, r2)) % self.mod


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
if n == 1:
    print(0, a[0] ^ b[0])
    return
x = [a[n - 1] ^ a[0]]
y = [b[n - 1] ^ b[0]]
for i in range(n - 1):
    x.append(a[i] ^ a[i + 1])
    y.append(b[i] ^ b[i + 1])

rh1_x, rh1_y = RollingHash(x, BASE, MOD1), RollingHash(y, BASE, MOD1)
rh2_x, rh2_y = RollingHash(x, BASE, MOD2), RollingHash(y, BASE, MOD2)
for k in range(n):
    if rh1_y.concatenate(n - k, n, 0, n - k) == rh1_x.get(0, n) and rh2_y.concatenate(n - k, n, 0, n - k) == rh2_x.get(0, n):
        print(k, a[0] ^ b[(n - k) % n])
