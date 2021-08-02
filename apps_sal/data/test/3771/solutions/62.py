# 最大流
import queue
NUMERIC_LIMITS = 10 ** 18


class maxFlow:
    class edge:
        def __init__(s, frm, to, cap, flow):
            s.frm, s.to = frm, to
            s.cap, s.flow = cap, flow

    def __init__(s, n):
        s._n = n
        s.g = [[] for _ in range(n)]
        s.pos = []

    def add_edge(s, frm, to, cap):
        m = len(s.pos)
        s.pos.append([frm, len(s.g[frm])])
        s.g[frm].append(s._edge(to, len(s.g[to]), cap))
        s.g[to].append(s._edge(frm, len(s.g[frm]) - 1, 0))
        return m

    def get_edge(s, i):
        m = len(s.pos)
        _e = s.g[s.pos[i][0]][s.pos[i][1]]
        _re = s.g[_e.to][_e.rev]
        return s.edge(s.pos[i][0], _e.to, _e.cap + _re.cap, _re.cap)

    def edges(s):
        m = len(s.pos)
        result = []
        for i in range(m):
            result.append(s.get_edge(i))
        return result

    def change_edge(s, i, new_cap, new_flow):
        m = len(s.pos)
        _e = s.g[s.pos[i].to][s.pos[i].rev]
        _re = s.g[_e.to][_e.rev]
        _e.cap = new_cap - new_flow
        _re.cap = new_flow

    def flow(self, s, t, flow_limit=NUMERIC_LIMITS):
        level = [0] * self._n
        iter = [0] * self._n

        def bfs():
            for i in range(self._n):
                level[i] = -1
            level[s] = 0
            que = queue.Queue()
            que.put(s)
            while not que.empty():
                v = que.get()
                for e in self.g[v]:
                    if e.cap == 0 or level[e.to] >= 0: continue
                    level[e.to] = level[v] + 1
                    if e.to == t: return
                    que.put(e.to)

        def dfs(this, v, up):
            if v == s: return up
            res = 0
            level_v = level[v]
            for i in range(iter[v], len(self.g[v])):
                e = self.g[v][i]
                if level_v <= level[e.to] or self.g[e.to][e.rev].cap == 0: continue
                d = this(this, e.to, min(up - res, self.g[e.to][e.rev].cap))
                if d <= 0: continue
                self.g[v][i].cap += d
                self.g[e.to][e.rev].cap -= d
                res += d
                if res == up: break
            return res

        flow = 0
        while flow < flow_limit:
            bfs()
            if level[t] == -1: break
            for i in range(self._n): iter[i]
            while flow < flow_limit:
                f = dfs(dfs, t, flow_limit - flow)
                if not f: break
                flow += f
        return flow

    def min_cut(self, s):
        visited = [False] * self._n
        que = queue.Queue()
        que.put(s)
        while not que.empty():
            p = que.get()
            visited[p] = True
            for e in self.g[p]:
                if e.cap and not visited[e.to]:
                    visited[e.to] = True
                    que.put(e.to)
        return visited

    class _edge:
        def __init__(s, to, rev, cap):
            s.to, s.rev = to, rev
            s.cap = cap


H, W = list(map(int, input().split()))
a = [list(input()) for _ in range(H)]

flow = maxFlow(H + W + 2)
s = H + W
t = H + W + 1
for h in range(H):
    for w in range(W):
        if a[h][w] == "S":
            flow.add_edge(s, h, H + W + 1)
            flow.add_edge(s, H + w, H + W + 1)
        elif a[h][w] == "T":
            flow.add_edge(h, t, H + W + 1)
            flow.add_edge(H + w, t, H + W + 1)
        if a[h][w] != ".":
            flow.add_edge(h, H + w, 1)
            flow.add_edge(H + w, h, 1)

ans = flow.flow(s, t)
if ans > H + W:
    print((-1))
else:
    print(ans)
