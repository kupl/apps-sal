from collections import defaultdict

INF = float("inf")

N, *A = map(int, open(0).read().split())

dp = defaultdict(lambda: -INF)
dp[(0, 0, False)] = 0

for i, a in enumerate(A, 1):
    p = i // 2
    for j in [p - 1, p, p + 1]:
        dp[(i, j, True)] = a + dp[(i - 1, j - 1, False)]
        dp[(i, j, False)] = max(dp[(i - 1, j, False)], dp[(i - 1, j, True)])

print(max(dp[(N, N // 2, True)], dp[(N, N // 2, False)]))
