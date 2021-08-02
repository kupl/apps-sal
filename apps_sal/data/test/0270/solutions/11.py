import sys
input = sys.stdin.readline
EPS = 10**(-8)
INF = 10**16

N, M = map(int, input().split())
graph = [set() for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a - 1].add(b - 1)

dp = [0] * N
dps = [0] * N
dpl = [0] * N
for n in reversed(range(N - 1)):
    for p in graph[n]:
        if dp[p] != -1:
            dps[n] += dp[p]
            dpl[n] += 1
    if dpl[n] > 0:
        dp[n] = dps[n] / dpl[n] + 1
    else:
        dp[n] = -1

Weight = [0] * N
Weight[0] = 1
for n in range(N):
    for p in graph[n]:
        Weight[p] += Weight[n] / dpl[n]

ans = dp[0]
for n1 in range(N):
    if len(graph[n1]) != 1:
        for n2 in graph[n1]:
            newE = (dps[n1] - dp[n2]) / (dpl[n1] - 1) + 1
            ans = min(ans, dp[0] - Weight[n1] * dp[n1] + Weight[n1] * newE)

print(ans)
