import heapq

class mcf_graph_int_cost:

    def __init__(self, n):
        self.n = n
        self.pos = []
        self.g = [[] for _ in range(n)]


    def add_edge(self, from_, to, cap, cost):
        # assert 0 <= from_ < self.n
        # assert 0 <= to < self.n
        m = len(self.pos)
        self.pos.append((from_, len(self.g[from_])))
        self.g[from_].append(self.__class__._edge(to, len(self.g[to]), cap, cost))
        self.g[to].append(self.__class__._edge(from_, len(self.g[from_]) - 1, 0, -cost))
        return m


    class edge:
        def __init__(self, from_, to, cap, flow, cost):
            self.from_ = from_
            self.to = to
            self.cap = cap
            self.flow = flow
            self.cost = cost


    def get_edge(self, i):
        _e = self.g[self.pos[i][0]][self.pos[i][1]]
        _re = self.g[_e.to][_e.rev]
        return self.__class__.edge(self.pos[i][0], _e.to, _e.cap + _re.cap, _re.cap, _e.cost)


    def edges(self):
        ret = []
        for i in range(len(self.pos)):
            _e = self.g[self.pos[i][0]][self.pos[i][1]]
            _re = self.g[_e.to][_e.rev]
            ret.append(self.__class__.edge(self.pos[i][0], _e.to, _e.cap + _re.cap, _re.cap, _e.cost))
        return ret


    def _dual_ref(self, s, t):
        self.dist = [4294967295] * self.n
        self.pv = [-1] * self.n
        self.pe = [-1] * self.n
        self.vis = [False] * self.n

        que = [s] # s ==  (0 << 32) + s 
        self.dist[s] = 0
        while que:
            v = heapq.heappop(que) & 4294967295
            if self.vis[v]:
                continue
            self.vis[v] = True
            if v == t:
                break
            for i in range(len(self.g[v])):
                e = self.g[v][i]
                if self.vis[e.to] or e.cap == 0:
                    continue
                cost = e.cost - self.dual[e.to] + self.dual[v]
                if self.dist[e.to] > self.dist[v] + cost:
                    self.dist[e.to] = self.dist[v] + cost
                    self.pv[e.to] = v
                    self.pe[e.to] = i
                    heapq.heappush(que, ((self.dist[e.to] << 32) + e.to))
        if not self.vis[t]:
            return False

        for v in range(self.n):
            if not self.vis[v]:
                continue
            self.dual[v] -= self.dist[t] - self.dist[v]
        
        return True


    def slope(self, s, t, flow_limit=4294967295):
        # assert 0 <= s < self.n
        # assert 0 <= t < self.n
        # assert s != t
        
        self.dual = [0] * self.n
        self.dist = [4294967295] * self.n
        self.pv = [-1] * self.n
        self.pe = [-1] * self.n
        self.vis = [False] * self.n
        
        flow = 0
        cost = 0
        prev_cost = -1
        result = [(flow, cost)]
        while flow < flow_limit:
            if not self._dual_ref(s, t):
                break
            c = flow_limit - flow
            v = t
            while v != s:
                c = min(c, self.g[self.pv[v]][self.pe[v]].cap)
                v = self.pv[v]
            v = t
            while v != s:
                e = self.g[self.pv[v]][self.pe[v]]
                e.cap -= c
                self.g[v][e.rev].cap += c
                v = self.pv[v]
            d = -self.dual[s]
            flow += c
            cost += c * d
            if prev_cost == d:
                result.pop()
            result.append((flow, cost))
            prev_cost = cost
        return result


    def flow(self, s, t, flow_limit=4294967295):
        return self.slope(s, t, flow_limit)[-1]

    
    class _edge:
        def __init__(self, to, rev, cap, cost):
            self.to = to
            self.rev = rev
            self.cap = cap
            self.cost = cost

INF = 10 ** 9

n = int(input())
a1, a2, a3 = list(map(int, input().split()))
b1, b2, b3 = list(map(int, input().split()))

g = mcf_graph_int_cost(8)
g.add_edge(0, 1, a1, 0)
g.add_edge(0, 2, a2, 0)
g.add_edge(0, 3, a3, 0)
g.add_edge(4, 7, b1, 0)
g.add_edge(5, 7, b2, 0)
g.add_edge(6, 7, b3, 0)
for i in range(1, 4):
    for j in range(4, 7):
        cost = 1 if (j - i) % 3 == 1 else 0
        g.add_edge(i, j, INF, cost)

f, ans1 = g.flow(0, 7)

ans2 = min(a1, b2) + min(a2, b3) + min(a3, b1)
print(ans1, ans2)


