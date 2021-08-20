(n, m, k) = list(map(int, input().split()))
is_gov = [0] * (n + 1)
prt = [0] * (n + 1)
cnt_gov = [0] * (n + 1)
adj = [[] for _ in range(n + 1)]
if k == 1:
    arr = [int(input())]
else:
    arr = list(map(int, input().split()))
for i in arr:
    is_gov[i] = 1
for i in range(m):
    (u, v) = list(map(int, input().split()))
    adj[u].append(v)
    adj[v].append(u)


def dfs(u, p, ID):
    stk = [(u, p, ID)]
    while stk:
        (u, p, ID) = stk[-1]
        stk.pop()
        if prt[u] != 0:
            continue
        prt[u] = ID
        cnt_gov[ID] += 1
        for v in adj[u]:
            if v != p:
                stk.append((v, u, ID))


for i in range(1, n + 1):
    if is_gov[i] == 1:
        dfs(i, -1, i)
(max_nodes, res) = (0, 0)
for i in range(1, n + 1):
    if is_gov[i] == 1:
        res += cnt_gov[i] * (cnt_gov[i] - 1) // 2
        max_nodes = max(max_nodes, cnt_gov[i])
res -= max_nodes * (max_nodes - 1) // 2
max_nodes += prt.count(0) - 1
res += max_nodes * (max_nodes - 1) // 2
print(res - m)
