(N, A, B, C) = list(map(int, input().split()))
l = [int(input()) for i in range(N)]


def dfs(cur, a, b, c):
    if cur == N:
        return abs(a - A) + abs(b - B) + abs(c - C) - 30 if min(a, b, c) > 0 else float('inf')
    r1 = dfs(cur + 1, a, b, c)
    r2 = dfs(cur + 1, a + l[cur], b, c) + 10
    r3 = dfs(cur + 1, a, b + l[cur], c) + 10
    r4 = dfs(cur + 1, a, b, c + l[cur]) + 10
    return min(r1, r2, r3, r4)


print(dfs(0, 0, 0, 0))
