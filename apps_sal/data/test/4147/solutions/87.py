N, A, B, C = list(map(int, input().split()))

l = []
for i in range(N):
    l.append(int(input()))


def dfs(i, a, b, c):
    if i == N:
        if min(a, b, c) == 0:
            return float("INF")
        else:
            return abs(a - A) + abs(b - B) + abs(c - C)
    else:
        ans0 = dfs(i + 1, a, b, c)
        ans1 = dfs(i + 1, a + l[i], b, c) + (10 if a != 0 else 0)
        ans2 = dfs(i + 1, a, b + l[i], c) + (10 if b != 0 else 0)
        ans3 = dfs(i + 1, a, b, c + l[i]) + (10 if c != 0 else 0)
    return min(ans0, ans1, ans2, ans3)


print((dfs(0, 0, 0, 0)))
