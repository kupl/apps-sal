n = int(input())
d = {}
cost = []
for i in range(n):
    cost.append(n * [0])
for i in range(n - 1):
    u, v, c = list(map(int, input().split()))
    if u not in d:
        d[u] = []
    if v not in d:
        d[v] = []
    d[u].append(v)
    d[v].append(u)
    cost[u][v] = c
    cost[v][u] = c
khoroch = n * [0]
visit = n * [0]


def dfs(d, s, parent):
    nonlocal ans
    visit[s] = 1
    khoroch[s] = cost[parent][s] + khoroch[parent]
    # print(s,visit[s])
    ans = max(khoroch[s], ans)
    for x in d[s]:
        if(visit[x] == 0):
            dfs(d, x, s)


ans = 0
dfs(d, 0, 0)
print(ans)
