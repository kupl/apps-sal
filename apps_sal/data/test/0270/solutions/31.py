N, M = map(int, input().split())
ST = [tuple(map(int, input().split())) for i in range(M)]

es = [[] for _ in range(N)]
for s, t in ST:
    s, t = s - 1, t - 1
    es[s].append(t)

dp = [0] * N
for i in range(N - 2, -1, -1):
    s = 0
    for to in es[i]:
        s += dp[to]
    dp[i] = 1 + s / len(es[i])

pp = [0] * N
pp[0] = 1.0
for i in range(N - 1):
    l = len(es[i])
    for to in es[i]:
        pp[to] += pp[i] / l

ans = dp[0]
for i in range(N - 1):
    l = len(es[i])
    if l < 2: continue
    before = 0
    after_whole = 0
    for to in es[i]:
        before += dp[to] / l
        after_whole += dp[to] / (l - 1)
    for to in es[i]:
        after = after_whole - dp[to] / (l - 1)
        diff = (before - after) * pp[i]
        ans = min(ans, dp[0] - diff)
print(ans)
