n, A, B, C = list(map(int, input().split()))
l = [int(input()) for _ in range(n)]
INF = 10**9


def dfs(now, a, b, c):
    if now == n:
        return abs(a - A) + abs(b - B) + abs(c - C) - 30 if min(a, b, c) > 0 else INF
    way1 = dfs(now + 1, a, b, c)
    way2 = dfs(now + 1, a + l[now], b, c) + 10
    way3 = dfs(now + 1, a, b + l[now], c) + 10
    way4 = dfs(now + 1, a, b, c + l[now]) + 10
    return min(way1, way2, way3, way4)


print((dfs(0, 0, 0, 0)))
