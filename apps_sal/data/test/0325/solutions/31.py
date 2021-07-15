from collections import deque
import sys


class mEdge():

    def __init__(self, _from, _to, _cost):
        self.From = _from
        self.to = _to
        self.cost = _cost


class bellman_ford():
    def __init__(self, V):
        self.G = []
        self._V = N
        self._E = 0

    def add(self, _from, _to, _cost):
        self.G.append(mEdge(_from, _to, _cost))
        self._E += 1

    def shortest_path(self, s):
        d = [10**20]*(self._V+1)
        d[s] = 0
        for _ in range(self._V):
            flag = False
            for edge in self.G:
                newlen = d[edge.From]+edge.cost
                if newlen < d[edge.to]:
                    flag = True
                    d[edge.to] = newlen
            if not flag:
                break
        return d

    def have_negative_circle(self):
        d = [10**20]*(self._V+1)
        d[1] = 0
        for i in range(1, self._V+1):
            flag = False
            for edge in self.G:
                newlen = d[edge.From]+edge.cost
                if newlen < d[edge.to]:
                    flag = True
                    d[edge.to] = newlen
            if not flag:
                break
            if i == self._V:
                return True
        return False


# Coins Respawn
sys.setrecursionlimit(10**7)
N, M, P = map(int, input().split())
graph = []
d = deque()


from_1 = [[] for i in range(N+1)]
from_N = [[] for i in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    from_1[a].append(b)
    from_N[b].append(a)
    d.append((a, b, P-c))


accessible_1 = [False for i in range(N+1)]
accessible_N = [False for i in range(N+1)]


def dfs_1(s):
    accessible_1[s] = True
    for node in from_1[s]:
        if accessible_1[node] == False:
            dfs_1(node)


def dfs_N(s):
    accessible_N[s] = True
    for node in from_N[s]:
        if accessible_N[node] == False:
            dfs_N(node)


dfs_1(1)
dfs_N(N)

isok = [False for i in range(N+1)]
for i in range(N+1):
    if accessible_1[i] and accessible_N[i]:
        isok[i] = True
G = bellman_ford(N)

while d:
    p, q, weight = d.popleft()
    if isok[p] and isok[q]:
        G.add(p, q, weight)

if G.have_negative_circle():
    print(-1)
else:

    print(max(0, -G.shortest_path(1)[N]))
