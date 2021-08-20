(N, A, B, C) = map(int, input().split())
L = [int(input()) for _ in range(N)]
INF = 10 ** 9


def dfs(i, a, b, c):
    if i == N:
        if min(a, b, c) > 0:
            return abs(a - A) + abs(b - B) + abs(c - C) - 30
        else:
            return INF
    ret1 = dfs(i + 1, a, b, c)
    ret2 = dfs(i + 1, a + L[i], b, c) + 10
    ret3 = dfs(i + 1, a, b + L[i], c) + 10
    ret4 = dfs(i + 1, a, b, c + L[i]) + 10
    return min(ret1, ret2, ret3, ret4)


print(dfs(0, 0, 0, 0))
