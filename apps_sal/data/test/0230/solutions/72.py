class RollingHash():
    def __init__(self, s, base, mod):
        self.mod = mod
        self.pw = pw = [1] * (len(s) + 1)

        l = len(s)
        self.h = h = [0] * (l + 1)

        v = 0
        for i in range(l):
            h[i + 1] = v = (v * base + ord(s[i])) % mod
        v = 1
        for i in range(l):
            pw[i + 1] = v = v * base % mod

    def get(self, l, r):
        return (self.h[r] - self.h[l] * self.pw[r - l]) % self.mod

    def check(self, d):
        ma = {}
        for i in range(N - d + 1):
            p = self.get(i, i + d)
            if p in ma:
                if i - ma[p] >= d:
                    return True
            else:
                ma[p] = i
        return False


N = int(input())
S = str(input())

base1 = 1007
mod1 = 10**9 + 7

RH = RollingHash(S, base1, mod1)

left = 0
right = N // 2 + 1
while right - left > 1:
    mid = (left + right) // 2
    if RH.check(mid):
        left = mid
    else:
        right = mid

print(left)
