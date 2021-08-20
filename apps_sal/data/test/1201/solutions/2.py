from functools import lru_cache


def readints():
    return [int(obj) for obj in input().strip().split()]


class Solver:

    def main(self):
        n = readints()[0]
        (self.t, self.d, self.p) = ([], [], [])
        for i in range(n):
            (t1, d1, p1) = readints()
            self.t.append(t1)
            self.d.append(d1)
            self.p.append(p1)
        self.backtrack = []
        sd = max(self.d) + 1
        for i in range(n + 1):
            self.backtrack.append([])
            for j in range(sd):
                self.backtrack[i].append(0)
        triples = list(zip(self.t, self.d, self.p, list(range(1, n + 1))))
        triples = sorted(triples, key=lambda x: x[1])
        (self.t, self.d, self.p, self.indexes) = ([0], [0], [0], [])
        for i in range(n):
            self.t.append(triples[i][0])
            self.d.append(triples[i][1])
            self.p.append(triples[i][2])
            self.indexes.append(triples[i][3])
        self.f = []
        for i in range(n + 1):
            self.f.append([])
            for j in range(sd):
                self.f[i].append(0)
        for i in range(1, n + 1):
            for d in range(sd):
                if d - self.t[i] >= 0 and d < self.d[i] and (self.t[i] < self.d[i]):
                    data = self.f[i - 1][d - self.t[i]]
                    if data + self.p[i] > self.f[i][d]:
                        self.f[i][d] = data + self.p[i]
                        self.backtrack[i][d] = i
                data = self.f[i - 1][d]
                if data > self.f[i][d]:
                    self.f[i][d] = data
                    self.backtrack[i][d] = 0
        ans = 0
        res = []
        best = None
        for i in range(sd):
            data = self.f[n][i]
            if data > ans:
                ans = data
                best = (n, i)
        if best is None:
            print('0\n0\n')
            return
        i = best[0]
        s = best[1]
        while i > 0:
            if self.backtrack[i][s] != 0:
                res.append(self.backtrack[i][s])
                s -= self.t[self.backtrack[i][s]]
            i -= 1
        print(ans)
        print(len(res))
        print(' '.join((str(self.indexes[item - 1]) for item in reversed(res))))


Solver().main()
