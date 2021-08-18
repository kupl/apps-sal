from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = 10**100
MAX = 2500
N, M, S = list(map(int, input().split()))
S = min(S, MAX)
G = [[] for _ in [0] * N]
C = []
for _ in [0] * M:
    u, v, a, b = list(map(int, input().split()))
    u -= 1
    v -= 1
    G[v].append((u, a, b))
    G[u].append((v, a, b))

for i in range(N):
    a, b = list(map(int, input().split()))
    C.append((a, b))

dp = [[INF] * MAX for _ in [0] * N]
q = []


def push(t, s, v):
    if s < 0:
        return
    if s >= MAX:
        s = MAX - 1
    if dp[v][s] <= t:
        return
    dp[v][s] = t
    heappush(q, (t, s, v))


push(0, S, 0)

while q:
    t, s, v = heappop(q)
    if dp[v][s] != t:
        continue

    c, d = C[v]
    push(t + d, s + c, v)

    for u, a, b in G[v]:
        push(t + b, s - a, u)

for d in dp[1:]:
    ans = INF
    for s in range(MAX):
        if ans > d[s]:
            ans = d[s]
    print(ans)
