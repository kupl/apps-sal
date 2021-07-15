def main():
    n, m = list(map(int, input().split()))
    n += 1
    children = [[] for _ in range(n)]
    degree, depth = [0] * n, [1] * n
    for _ in range(m):
        u, v = list(map(int, input().split()))
        if u < v:
            children[u].append(v)
        else:
            children[v].append(u)
        degree[u] += 1
        degree[v] += 1
    for a, c in zip(depth, children):
        for v in c:
            if depth[v] <= a:
                depth[v] = a + 1
    print(max(a * b for a, b in zip(depth, degree)))


def __starting_point():
    main()

__starting_point()
