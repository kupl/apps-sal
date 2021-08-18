N, A, B, C = map(int, input().split())
l = [int(input()) for i in range(N)]
INF = 10 ** 9


def dfs(cnt, a, b, c):
    if cnt == N:
        return abs(a - A) + abs(b - B) + abs(c - C) - 30 if min(a, b, c) > 0 else INF
    res0 = dfs(cnt + 1, a, b, c)
    res1 = dfs(cnt + 1, a + l[cnt], b, c) + 10
    res2 = dfs(cnt + 1, a, b + l[cnt], c) + 10
    res3 = dfs(cnt + 1, a, b, c + l[cnt]) + 10
    return min(res0, res1, res2, res3)


print(dfs(0, 0, 0, 0))
