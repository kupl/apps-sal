class CF574B:
    M = int(1e12)

    def __init__(self):
        n, m = list(map(int, input().split()))
        self.graph = [set() for _ in range(n + 1)]
        self.edges = []
        for _ in range(m):
            a, b = list(map(int, input().split()))
            self.edges += [(a, b)]
            self.graph[a] |= {b}
            self.graph[b] |= {a}

    def solve(self):
        res = self.M
        for a, b in self.edges:
            for common in self.graph[a] & self.graph[b]:
                res = min(res, len(self.graph[a]) + len(self.graph[b]) + len(self.graph[common]) - 6)
        print(res if res < self.M else -1)


def main():
    CF574B().solve()


def __starting_point():
    main()


__starting_point()
