import sys
sys.setrecursionlimit(1500)

MAX = 100005;
g = [[] for _ in range(MAX)]
vis = [False] * MAX
dp = [0] * MAX
prod = [0] * MAX

edges = []
order = []


def dfs(st):
    stack = []
    stack.append((st, -1))
    vis[st] = True
    while stack:
        st, parent = stack.pop()
        order.append(st)
        vis[st] = True
        if (st == parent): continue;
        for i in g[st]:
            if (vis[i[0]]): continue;
            stack.append((i[0], st))


n = int(input())
for i in range(n - 1):
    a, b, w = list(map(int, sys.stdin.readline().split(' ')))
    g[a].append([b, w])
    g[b].append([a, w])
    edges.append([[a, b], w])

dfs(1);
order.reverse()
for st in order:
    dp[st] = 1;
    for i in g[st]:
        dp[st] += dp[i[0]];
tot = 0;
curr = 1;
div = n * (n - 1) / 2;
for i in edges:
    a = i[0][0];
    b = i[0][1];
    sa = dp[a];
    sb = dp[b];
    tot += min(sa, sb) * (n - min(sa, sb)) * i[1];
    prod[curr] = min(sa, sb) * (n - min(sa, sb));
    curr += 1;

q = int(input())
for i in range(q):
    q1, q2 = list(map(int, sys.stdin.readline().split(' ')))
    tot -= prod[q1] * edges[q1 - 1][1];
    edges[q1 - 1][1] = q2;
    tot += prod[q1] * edges[q1 - 1][1];
    sys.stdout.write(str(tot * 3 / div) + "\n")
