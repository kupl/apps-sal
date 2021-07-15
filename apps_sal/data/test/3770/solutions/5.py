import sys
readline = sys.stdin.readline
import collections
class Dinic:
    def __init__(self, vnum):
        self.edge = [[] for i in range(vnum)]
        self.n = vnum
        # infはint型の方が良いかもね
        self.inf = 10**9+7
    def addedge(self, st, en, c):
        self.edge[st].append([en, c, len(self.edge[en])])
        self.edge[en].append([st, 0, len(self.edge[st])-1])
    def bfs(self, vst):
        dist = [-1]*self.n
        dist[vst] = 0
        Q = collections.deque([vst])
        while Q:
            nv = Q.popleft()
            for vt, c, r in self.edge[nv]:
                if dist[vt] == -1 and c > 0:
                    dist[vt] = dist[nv] + 1
                    Q.append(vt)
        self.dist = dist
    def dfs(self, nv, en, nf):
        nextv = self.nextv
        if nv == en:
            return nf
        dist = self.dist
        ist = nextv[nv]
        for i, (vt, c, r) in enumerate(self.edge[nv][ist:], ist):
            if dist[nv] < dist[vt] and c > 0:
                df = self.dfs(vt, en, min(nf, c))
                if df > 0:
                    self.edge[nv][i][1] -= df
                    self.edge[vt][r][1] += df
                    return df
            nextv[nv] += 1
        return 0
    def getmf(self, st, en):
        mf = 0
        while True:
            self.bfs(st)
            if self.dist[en] == -1:
                break
            self.nextv = [0]*self.n
            while True:
                fl = self.dfs(st, en, self.inf)
                if fl > 0:
                    mf += fl
                else:
                    break
        return mf


N, M = list(map(int, readline().split()))
A = list(map(int, readline().split()))
B = list(map(int, readline().split()))


INF = 10**9+7
D = Dinic(2*N+2)
st = 2*N
en = st+1

ans = 0
for i in range(N):
    b = abs(B[i])
    if B[i] < 0:
        D.addedge(st, 2*i, 2*b)
    else:
        D.addedge(2*i+1, en, 2*b)
    D.addedge(2*i, 2*i+1, A[i] + b)
    ans += b

for _ in range(M):
    u, v = list(map(int, readline().split()))
    u -= 1
    v -= 1
    D.addedge(2*u+1, 2*v, INF)
    D.addedge(2*v+1, 2*u, INF)

print((ans - D.getmf(st, en)))
    

