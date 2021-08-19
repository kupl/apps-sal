def main():
    (n, m) = list(map(int, input().split()))
    n += 1
    children = [0] * n
    degree = [0] * n
    for _ in range(m):
        (u, v) = list(map(int, input().split()))
        if u > v:
            (u, v) = (v, u)
        l = children[u]
        if l:
            l.append(v)
        else:
            children[u] = [v]
        degree[u] += 1
        degree[v] += 1
    depth = [1] * n
    for (a, c) in zip(depth, children):
        if a and c:
            a += 1
            for v in c:
                if depth[v] < a:
                    depth[v] = a
    print(max((a * b for (a, b) in zip(depth, degree))))


def __starting_point():
    main()


__starting_point()
