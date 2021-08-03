import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15


def main():
    MAXS = 100005
    N = int(input())
    X = [set() for _ in range(MAXS)]
    Y = [set() for _ in range(MAXS)]
    for _ in range(N):
        x, y = map(int, input().split())
        X[x].add(y)
        Y[y].add(x)

    used_x = [0] * MAXS
    used_y = [0] * MAXS
    ans = -N
    for i in range(MAXS):
        if used_x[i]:
            continue
        used_x[i] = 1
        if not X[i]:
            continue
        max_height = set(X[i])
        max_width = {i}
        stack = [(i, 0)]
        while stack:
            v, typ = stack.pop()
            if typ == 0:
                for y in X[v]:
                    if used_y[y]:
                        continue
                    used_y[y] = 1
                    if Y[y]:
                        max_width |= Y[y]
                        stack.append((y, 1))
            else:
                for x in Y[v]:
                    if used_x[x]:
                        continue
                    used_x[x] = 1
                    if X[x]:
                        max_height |= X[x]
                        stack.append((x, 0))
        ans += len(max_width) * len(max_height)
    print(ans)


def __starting_point():
    main()


__starting_point()
