import sys
(n, m, k) = list(map(int, input().split()))
castle = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
_p = [[] for _ in range(n)]
endpoints = [0] * n
for (u, v) in (list(map(int, l.split())) for l in sys.stdin):
    _p[v - 1].append(u - 1)
    endpoints[v - 1] = 1
portal = [[] for _ in range(n)]
for t in range(n):
    if _p[t]:
        s = max(_p[t])
        portal[s].append(castle[t][2])
max_n = 5000
dp = [-1] * (max_n + 1)
dp[k] = 0
for (i, (a, b, c)) in enumerate(castle):
    next_dp = [-1] * (max_n + 1)
    p = portal[i]
    if not endpoints[i]:
        p.append(c)
    p.sort(reverse=True)
    for i in range(len(p) - 1):
        p[i + 1] += p[i]
    p = [0] + p
    len_p = len(p)
    for i in range(a, max_n - b + 1):
        if dp[i] == -1:
            continue
        w = i + b
        for j in range(len_p):
            next_dp[w - j] = max(next_dp[w - j], dp[i] + p[j])
            if w - j == 0:
                break
    dp = next_dp
print(max(dp))
