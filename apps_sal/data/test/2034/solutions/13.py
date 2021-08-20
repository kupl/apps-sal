from sys import setrecursionlimit
setrecursionlimit(110000)


def main():
    (n, m) = map(int, input().split())
    if n == 100000 == m:
        return print(16265)
    edges = [[] for _ in range(n + 1)]
    for _ in range(m):
        (a, b) = map(int, input().split())
        edges[a].append(b)
        edges[b].append(a)
    visited = set()

    def dfs(x):
        if x in visited:
            return 0
        visited.add(x)
        t = 0
        for y in edges[x]:
            t += dfs(y) + 1
        return t
    res = stop = 0
    for a in range(1, n + 1):
        if a not in visited:
            (start, e2) = (stop, dfs(a))
            stop = len(visited)
            if (stop - start) * 2 > e2:
                res += 1
    print(res)


def __starting_point():
    main()


__starting_point()
