import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()

class MaxFlow(object):
    def __init__(self, n):
        self.n = n
        self.E = [[] for _ in range(n)]

    def add_edge(self, u, v, cap):
        e = [v, cap, 0]
        rev = [u, 0, e]
        e[-1] = rev
        self.E[u].append(e)
        self.E[v].append(rev)

    def _bfs(self, s, t):
        self._level = level = [-1] * self.n
        level[s] = 0
        queue = [s]
        for v in queue:
            for nv, cap, _ in self.E[v]:
                if cap and level[nv] == -1:
                    level[nv] = level[v] + 1
                    if nv == t:
                        return True
                    queue.append(nv)
        return level[t] != -1

    def _dfs(self, s, t):
        E, level, it = self.E, self._level, self._iter
        stack = [(s, INF)]
        while stack:
            v, f = stack[-1]
            if v == t:
                for v, _ in stack[:-1]:
                    E[v][it[v]][1] -= f
                    E[v][it[v]][-1][1] += f
                return f
            while it[v] < len(E[v]):
                nv, cap, _ = E[v][it[v]]
                if cap and level[v] < level[nv]:
                    stack.append((nv, min(f, cap)))
                    break
                it[v] += 1
            else:
                stack.pop()
                level[v] = 0
        return 0

    def solve(self, s, t):
        res = 0
        while self._bfs(s, t):
            self._iter = [0] * self.n
            f = 1
            while f:
                f = self._dfs(s, t)
                res += f
        return res

from itertools import product
def resolve():
    m, n = map(int, input().split())
    grid = [input() for _ in range(m)]
    N = m + n
    flow = MaxFlow(N + 2)

    for i, j in product(range(m), range(n)):
        if grid[i][j] == 'S':
            flow.add_edge(i, j + m, INF)
            flow.add_edge(j + m, i, INF)
            flow.add_edge(N, i, INF)
            flow.add_edge(N, j + m, INF)
        elif grid[i][j] == 'T':
            flow.add_edge(i, j + m, INF)
            flow.add_edge(j + m, i, INF)
            flow.add_edge(i, N + 1, INF)
            flow.add_edge(j + m, N + 1, INF)
        elif grid[i][j] != '.':
            flow.add_edge(i, j + m, 1)
            flow.add_edge(j + m, i, 1)

    ans = flow.solve(N, N + 1)
    if ans > 10 << 30:
        ans = -1
    print(ans)
resolve()
