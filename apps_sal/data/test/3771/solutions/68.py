from collections import deque


class MF_graph(object):

    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]
        self.pos = []

    def add_edge(self, frm, to, cap):
        m = len(self.pos)
        self.pos.append((frm, len(self.g[frm])))
        self.g[frm].append([to, len(self.g[to]), cap])
        self.g[to].append([frm, len(self.g[frm]) - 1, 0])
        return m

    def get_edge(self, i):
        (e_to, e_rev, e_cap) = self.g[self.pos[i][0]][self.pos[i][1]]
        (re_to, _, re_cap) = self.g[e_to][e_rev]
        return (re_to, e_to, e_cap + re_cap, re_cap)

    def edges(self):
        m = len(self.pos)
        for i in range(m):
            yield self.get_edge(i)

    def change_edge(self, i, new_cap, new_flow):
        (f, s) = self.pos[i]
        (rf, rs, _) = self.g[f][s]
        self.g[f][s][2] = new_cap - new_flow
        self.g[rf][rs][2] = new_flow
        return

    def dfs(self, s, v, up):
        if v == s:
            return up
        res = 0
        level_v = self.level[v]
        for i in range(self.iter[v], len(self.g[v])):
            (u_to, u_rev, _) = self.g[v][i]
            if level_v <= self.level[u_to] or self.g[u_to][u_rev][2] == 0:
                continue
            d = self.dfs(s, u_to, min(up - res, self.g[u_to][u_rev][2]))
            if d <= 0:
                continue
            self.g[v][i][2] += d
            self.g[u_to][u_rev][2] -= d
            res += d
            if res == up:
                break
        return res

    def flow(self, s, t, flow_limit=10 ** 18):
        self.iter = [0] * self.n
        flow = 0
        while flow < flow_limit:
            self.level = [-1] * self.n
            self.level[s] = 0
            que = deque([s])
            while que:
                v = que.popleft()
                for (u_to, _, u_cap) in self.g[v]:
                    if u_cap == 0 or self.level[u_to] >= 0:
                        continue
                    self.level[u_to] = self.level[v] + 1
                    if u_to == t:
                        break
                    que.append(u_to)
            if self.level[t] == -1:
                break
            self.iter = [0] * self.n
            while flow < flow_limit:
                f = self.dfs(s, t, flow_limit - flow)
                if not f:
                    break
                flow += f
        return flow

    def min_cut(self, s):
        visited = [False] * self.n
        que = deque([s])
        while que:
            v = que.popleft()
            visited[v] = True
            for (u_to, _, u_cap) in self.g[v]:
                if u_cap and (not visited[u_to]):
                    visited[u_to] = True
                    que.append(u_to)
        return visited


(H, W) = map(int, input().split())
S = [input() for _ in range(H)]
inf = 10 ** 18
g = MF_graph(H + W + 2)
source = H + W
sink = H + W + 1
for i in range(H):
    for j in range(W):
        if S[i][j] == 'S':
            g.add_edge(source, i, inf)
            g.add_edge(source, H + j, inf)
        elif S[i][j] == 'T':
            g.add_edge(i, sink, inf)
            g.add_edge(H + j, sink, inf)
        elif S[i][j] == 'o':
            g.add_edge(i, H + j, 1)
            g.add_edge(H + j, i, 1)
flow = g.flow(source, sink)
if flow >= inf:
    print(-1)
else:
    print(flow)
