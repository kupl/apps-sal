from math import inf
from sys import setrecursionlimit

setrecursionlimit(10**4)

N, K = map(int, input().split())
P = [0] + list(map(int, input().split()))
C = [0] + list(map(int, input().split()))


class Graph(list):
    def __init__(self, n):
        super().__init__([None] * (n + 1))
        self.directions = P
        self.points = C
        self.loops = []
        self.loopscores = []
        self.search()
        self.evalloop()

    def search(self):
        for i in range(1, len(self)):
            self.history = set()
            self.goto(i)

    def goto(self, i):
        if self[i]:
            return self[i]
        if i in self.history:
            return self.addloop(i)
        self.history.add(i)
        l, p = self.goto(self.directions[i])
        if self[i] == None:
            self[i] = (l, p + 1)
        return self[i]

    def addloop(self, j):
        loop = [j]
        k = self.directions[j]
        while j != k:
            loop.append(k)
            k = self.directions[k]
        self.loops.append(loop)
        l = len(self.loops) - 1
        for i in loop:
            self[i] = (l, 0)
        return (l, 0)

    def maxscore(self):
        return max(self.score(self.directions[i], K) for i in range(1, len(self)))

    def score(self, i, k):
        if k == 0:
            return 0
        p = self.points[i]
        i = self.directions[i]
        k -= 1
        if self[i][1] > 0:
            s = self.score(i, k)
            return p + max(0, s)
        n = self[i][0]
        loop = self.loops[n]
        j = loop.index(i)
        base = self.base[n]
        loopscore = base[-1]
        leftmax = self.leftmax[n]
        rightmax = self.rightmax[n]
        length = len(loop)
        d, m = divmod(k, length)
        if m == 0:
            s = 0
        elif j + m < length:
            if leftmax[j] < leftmax[j + m]:
                s = leftmax[j + m] - base[j]
            elif rightmax[j + 1] > rightmax[j + m + 1]:
                s = rightmax[j + 1] - base[j]
            else:
                s = max(base[j + 1:j + m + 1]) - base[j]
        else:
            s = max(loopscore + leftmax[j + m - length], rightmax[j + 1]) - base[j]
        if d:
            t = max(loopscore + leftmax[j], rightmax[j + 1]) - base[j]
            return max(0, s, s + loopscore * d, t, t + loopscore * (d - 1)) + p
        else:
            return max(0, s, s + loopscore * d) + p

    def evalloop(self):
        b, c, d = [], [], []
        for l in self.loops:
            bb, cc, dd = [0], [-inf], [-inf]
            for i in l:
                bb.append(bb[-1] + self.points[i])
            for v in bb:
                cc.append(max(cc[-1], v))
            for v in reversed(bb):
                dd.append(max(dd[-1], v))
            b.append(bb)
            c.append(cc[1:])
            d.append(list(reversed(dd[1:])))
        self.base = b
        self.leftmax = c
        self.rightmax = d


g = Graph(N)
print(g.maxscore())
