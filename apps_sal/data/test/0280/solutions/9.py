from itertools import permutations

N, M, *I = map(int, open(0).read().split())
W, LV = I[:N], list(zip(*[iter(I[N:])] * 2))

if any(w > v for _, v in LV for w in W):
    print(-1)
    return

L = [0] * (1 << N)
for i in range(1 << N):
    s = sum(w for j, w in enumerate(W) if i >> j & 1)
    L[i] = max((l for l, v in LV if s > v), default=0)

ans = float("inf")
for P in permutations(range(N)):
    dp = [0] * N
    for i, p in enumerate(P[1:], 1):
        t = 1 << p
        for j in reversed(range(i)):
            t |= 1 << P[j]
            dp[i] = max(dp[i], dp[j] + L[t])
    ans = min(ans, dp[-1])

print(ans)
