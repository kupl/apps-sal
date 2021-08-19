n = int(input())
adj = [[[], 0, 0] for i in range(n)]
for i in range(n - 1):
    (u, v) = map(int, input().split())
    adj[u - 1][0].append(v - 1)
    adj[v - 1][0].append(u - 1)
queue = [0]
while queue:
    curr_v = queue.pop(0)
    adj[curr_v][2] = 1
    for u in adj[curr_v][0]:
        if not adj[u][2]:
            queue.append(u)
            adj[u][1] = adj[curr_v][1] + 1
ev = 0
n_ev = 0
for el in adj:
    if el[1] % 2 == 0:
        ev += 1
    else:
        n_ev += 1
ans = 0
for el in adj:
    if el[1] % 2 == 0:
        ans += n_ev - len(el[0])
    else:
        ans += ev - len(el[0])
print(ans // 2)
