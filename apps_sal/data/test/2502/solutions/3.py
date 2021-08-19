class RollingHash:

    def __init__(self, s, base, mod):
        self.mod = mod
        l = len(s)
        self.pw = pw = [1] * (l + 1)
        self.h = h = [0] * (l + 1)
        for i in range(l):
            h[i + 1] = (h[i] * base + ord(s[i])) % mod
            pw[i + 1] = pw[i] * base % mod

    def get(self, l, r):
        return (self.h[r] - self.h[l] * self.pw[r - l]) % self.mod


def main():
    s = input()
    t = input()
    (ls, lt) = (len(s), len(t))
    m = (ls + lt - 1) // ls + 1
    s *= m
    s1 = RollingHash(s, 1007, 10 ** 9 + 7)
    t1 = RollingHash(t, 1007, 10 ** 9 + 7)
    w = t1.get(0, lt)
    g = [None] * ls
    for i in range(ls):
        if s1.get(i, i + lt) == w:
            g[i] = (i + lt) % ls
    f = [None] * ls
    for i in range(ls):
        if f[i] is None:
            f[i] = ls
            q = [i]
            while q:
                if g[q[-1]] is None:
                    f[q[-1]] = 0
                    q.pop()
                elif f[g[q[-1]]] is None:
                    q.append(g[q[-1]])
                else:
                    f[q[-1]] = f[g[q[-1]]] + 1
                    q.pop()
    print(max(f) if max(f) < ls else -1)
    return


main()
