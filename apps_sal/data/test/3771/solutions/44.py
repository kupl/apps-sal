from collections import deque
import sys
sys.setrecursionlimit(10 ** 7)


class MaxFlow:

    def __init__(self, n):
        self.n = n
        self.g = [[] for i in range(n)]

    def add_edge(self, fr, to, cap):
        forward = [to, cap, None]
        forward[2] = backward = [fr, 0, forward]
        self.g[fr].append(forward)
        self.g[to].append(backward)

    def bfs(self, s, t):
        self.level = level = [None] * self.n
        deq = deque([s])
        level[s] = 0
        g = self.g
        while deq:
            v = deq.popleft()
            nlv = level[v] + 1
            for (nv, cap, _) in g[v]:
                if cap and level[nv] is None:
                    level[nv] = nlv
                    deq.append(nv)
        return level[t] is not None

    def dfs(self, v, t, f):
        if v == t:
            return f
        level = self.level
        for e in self.it[v]:
            (nv, cap, rev) = e
            if cap and level[v] < level[nv]:
                d = self.dfs(nv, t, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0

    def flow(self, s, t):
        flow = 0
        INF = 10 ** 9 + 7
        g = self.g
        while self.bfs(s, t):
            (*self.it,) = list(map(iter, self.g))
            f = INF
            while f:
                f = self.dfs(s, t, INF)
                flow += f
        return flow


def main2(h, w, mat):
    ss = (-1, -1)
    tt = (-1, -1)
    n = h + w + 2
    g = [[] for _ in range(n)]
    ary = []
    inf = 10 ** 18
    for i in range(h):
        for j in range(w):
            if mat[i][j] == 'o':
                ary.append([i, h + j, 1])
                ary.append([h + j, i, 1])
            elif mat[i][j] == 'S':
                ary.append([h + w, i, inf])
                ary.append([i, h + w, inf])
                ary.append([h + w, h + j, inf])
                ary.append([h + j, h + w, inf])
                ss = (i, j)
            elif mat[i][j] == 'T':
                ary.append([h + w + 1, i, inf])
                ary.append([i, h + w + 1, inf])
                ary.append([h + w + 1, h + j, inf])
                ary.append([h + j, h + w + 1, inf])
                tt = (i, j)
    if ss[0] == tt[0] or ss[1] == tt[1]:
        return -1
    mf = MaxFlow(n)
    for (i, j, c) in ary:
        mf.add_edge(i, j, c)
    ret = mf.flow(h + w, h + w + 1)
    return ret


def __starting_point():
    (h, w) = list(map(int, input().split()))
    mat = [list(input()) for _ in range(h)]
    ret2 = main2(h, w, [x.copy() for x in mat])
    print(ret2)


__starting_point()
