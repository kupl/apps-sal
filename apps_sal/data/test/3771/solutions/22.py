def main():
    import sys
    input = sys.stdin.readline
    from collections import deque

    class Dinic:
        def __init__(self, N):
            self.N = N
            self.G = [[] for i in range(N)]

        def add_edge(self, fr, to, cap):
            forward = [to, cap, None]
            forward[2] = backward = [fr, 0, forward]
            self.G[fr].append(forward)
            self.G[to].append(backward)

        def add_multi_edge(self, v1, v2, cap1, cap2):
            edge1 = [v2, cap1, None]
            edge1[2] = edge2 = [v1, cap2, edge1]
            self.G[v1].append(edge1)
            self.G[v2].append(edge2)

        def bfs(self, s, t):
            self.level = level = [None] * self.N
            deq = deque([s])
            level[s] = 0
            G = self.G
            while deq:
                v = deq.popleft()
                lv = level[v] + 1
                for w, cap, _ in G[v]:
                    if cap and level[w] is None:
                        level[w] = lv
                        deq.append(w)
            return level[t] is not None

        def dfs(self, v, t, f):
            if v == t:
                return f
            level = self.level
            for e in self.it[v]:
                w, cap, rev = e
                if cap and level[v] < level[w]:
                    d = self.dfs(w, t, min(f, cap))
                    if d:
                        e[1] -= d
                        rev[1] += d
                        return d
            return 0

        def flow(self, s, t):
            flow = 0
            INF = 10 ** 9 + 7
            G = self.G
            while self.bfs(s, t):
                *self.it, = list(map(iter, self.G))
                f = INF
                while f:
                    f = self.dfs(s, t, INF)
                    flow += f
            return flow

    H, W = list(map(int, input().split()))
    grid = []
    for _ in range(H):
        line = input().rstrip('\n')
        grid.append(line)

    dinic = Dinic(H+W+5)
    for h in range(H):
        for w in range(W):
            if grid[h][w] == 'o':
                dinic.add_edge(h+1, H+w+1, 1)
                dinic.add_edge(H+w+1, h+1, 1)
            elif grid[h][w] == 'S':
                dinic.add_edge(H+W+1, h+1, 10**5)
                dinic.add_edge(H+W+1, H+w+1, 10**5)
            elif grid[h][w] == 'T':
                dinic.add_edge(h+1, H+W+2, 10**5)
                dinic.add_edge(H+w+1, H+W+2, 10**5)

    ans = dinic.flow(H+W+1, H+W+2)
    if ans > 400:
        print((-1))
    else:
        print(ans)


def __starting_point():
    main()

__starting_point()
