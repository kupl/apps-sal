from sys import stdin, setrecursionlimit


class Dinic:

    def __init__(self, v, inf=float("inf")):
        self.V = v
        self.inf = inf
        self.G = [[] for _ in range(v)]
        self.level = [0 for _ in range(v)]
        self.iter = [0 for _ in range(v)]

    def addEdge(self, fm, to, cap):
        '''
        to:行き先
        cap:容量
        rev:反対側の辺
        '''
        self.G[fm].append({'to': to, 'cap': cap, 'rev': len(self.G[to])})
        self.G[to].append({'to': fm, 'cap': 0, 'rev': len(self.G[fm]) - 1})

    # sからの最短距離をbfsで計算

    def bfs(self, s):
        import queue
        self.level = [-1 for _ in range(self.V)]
        self.level[s] = 0
        que = queue.Queue()
        que.put(s)

        while not que.empty():
            v = que.get()
            for i in range(len(self.G[v])):
                e = self.G[v][i]
                if e['cap'] > 0 and self.level[e['to']] < 0:
                    self.level[e['to']] = self.level[v] + 1
                    que.put(e['to'])

    def dfs(self, v, t, f):
        if v == t:
            return f
        for i in range(self.iter[v], len(self.G[v])):
            self.iter[v] = i
            e = self.G[v][i]
            if e['cap'] > 0 and self.level[v] < self.level[e['to']]:
                d = self.dfs(e['to'], t, min(f, e['cap']))
                if d > 0:
                    e['cap'] -= d
                    self.G[e['to']][e['rev']]['cap'] += d
                    return d
        return 0

    def max_flow(self, s, t):
        flow = 0
        while True:
            self.bfs(s)
            if self.level[t] < 0:
                return flow
            self.iter = [0 for _ in range(self.V)]
            f = self.dfs(s, t, self.inf)
            while f > 0:
                flow += f
                f = self.dfs(s, t, self.inf)


def IL(): return list(map(int, stdin.readline().split()))


setrecursionlimit(1000000)


def main():
    N = int(input())
    a = IL()
    d = Dinic(N + 2)
    res = 0
    for i in range(N):
        d.addEdge(N, i, max(0, -a[i]))
        d.addEdge(i, N + 1, max(0, a[i]))
        res += max(0, a[i])
        t = 2 * i + 2
        while t <= N:
            d.addEdge(i, t - 1, float('inf'))
            t += i + 1
    print(res - d.max_flow(N, N + 1))


def __starting_point(): main()


__starting_point()
