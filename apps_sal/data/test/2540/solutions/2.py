import sys
from collections import Counter

n = int(input())
color = list(map(int, input().split()))
adj = [[] for _ in range(n)]

for _ in range(n - 1):
    u, v = list(map(int, sys.stdin.readline().split()))
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)

count = [Counter() for _ in range(n)]
max_cnt = [0] * n
dp = [0] * n

stack = [0]
par = [-1] * n
order = []
while stack:
    v = stack.pop()
    order.append(v)
    for d in adj[v]:
        if d != par[v]:
            stack.append(d)
            par[d] = v

for v in reversed(order):
    child = [i for i in adj[v] if i != par[v]]
    child.sort(key=lambda v: -len(count[v]))

    if child:
        dp[v] = dp[child[0]]
        max_cnt[v] = max_cnt[child[0]]
        count[v] = count[child[0]]
        for d in child[1:]:
            for k, val in list(count[d].items()):
                count[v][k] += val
                if count[v][k] > max_cnt[v]:
                    dp[v] = k
                    max_cnt[v] = count[v][k]
                elif count[v][k] == max_cnt[v]:
                    dp[v] += k

    count[v][color[v]] += 1
    if count[v][color[v]] > max_cnt[v]:
        dp[v] = color[v]
        max_cnt[v] = count[v][color[v]]
    elif count[v][color[v]] == max_cnt[v]:
        dp[v] += color[v]

    if par[v] != -1:
        stack.append(par[v])

print(*dp)
