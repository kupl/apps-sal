def dp(H, N, ab):
    max_a = max([ab[i][0] for i in range(N)])
    d = [INF for _ in range(H + max_a)]
    d[0] = 0
    for h in range(1, H + max_a):
        d[h] = min(d[h - a] + b for a, b in ab)
    return min(d[H:])


INF = 10 ** 10
H, N = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(N)]
print(dp(H, N, ab))
