from collections import defaultdict


class Imos:
    def __init__(self, n):
        self.B = [0] * n
        self.n = n
        from itertools import accumulate
        self.ac = accumulate

    def __call__(self, l, r):
        l, r = max(l, 0), min(r, self.n - 1)
        self.B[l] += 1
        self.B[r + 1] -= 1

    def out(self):
        *res, = self.ac(self.B)
        return res


d = defaultdict(list)
imos = Imos(10 ** 5 + 1)

(N, C), *D = [[*map(int, o.split())] for o in open(0)]
for s, t, c in D:
    d[c] += (s, t),
for p in d.values():
    p.sort()
    ps, pt = p[0]
    for s, t in p[1:] + [[0, 0]]:
        if pt == s:
            pt = t
        else:
            imos(ps - 1, pt - 1)
            ps, pt = s, t
print(max(imos.out()))
