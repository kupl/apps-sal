3


class StdIO:

    def read_int(self):
        return int(self.read_string())

    def read_ints(self, sep=None):
        return [int(i) for i in self.read_strings(sep)]

    def read_float(self):
        return float(self.read_string())

    def read_floats(self, sep=None):
        return [float(i) for i in self.read_strings(sep)]

    def read_string(self):
        return input()

    def read_strings(self, sep=None):
        return self.read_string().split(sep)


io = StdIO()


def bfs(adj, vi, visited):
    q = [vi]
    visited[vi] = True
    vc = 0
    ec = 0
    while q:
        v = q.pop()
        vc += 1
        ec += len(adj[v])
        for u in adj[v]:
            if not visited[u]:
                q.append(u)
                visited[u] = True
    return (vc, ec // 2)


def main():
    (n, m) = io.read_ints()
    adj = [list() for i in range(n)]
    for i in range(m):
        (x, y) = io.read_ints()
        x -= 1
        y -= 1
        adj[x].append(y)
        adj[y].append(x)
    visited = [False] * n
    bad_cities = 0
    for v in range(n):
        if not visited[v]:
            (vc, ec) = bfs(adj, v, visited)
            if ec < vc:
                bad_cities += vc - ec
    print(bad_cities)


def __starting_point():
    main()


__starting_point()
