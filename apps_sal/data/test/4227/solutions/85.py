N, M = list(map(int, input().split()))
to = [[] for _ in range(N)]

for _ in range(M):
    a, b = list(map(int, input().split()))
    a, b = a - 1, b - 1
    to[a].append(b)
    to[b].append(a)


def dfs(v, seen):
    if seen == [1] * N:
        return 1

    res = 0
    for nv in to[v]:
        if not seen[nv]:
            seen[nv] = 1
            res += dfs(nv, seen)
            seen[nv] = 0
    return res


def main():
    seen = [0] * N
    seen[0] = 1
    print((dfs(0, seen)))


def __starting_point():
    main()


__starting_point()
