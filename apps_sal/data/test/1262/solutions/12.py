n = int(input())
pos = [[*map(int, input().split())] for i in range(n)]
*c, = map(int, input().split())
*k, = map(int, input().split())
used = [False for i in range(n)]
parent = [-1 for i in range(n)]
plants = []
connections = []
ans = 0
_n = n
while(_n):
    _n -= 1
    mn, u = min([(ci, i) for i, ci in enumerate(c) if not used[i]])
    ans += mn
    used[u] = True
    if parent[u] == -1:
        plants.append(u)
    else:
        connections.append((min(parent[u], u), max(parent[u], u)))
    for i in range(n):
        con_cost = (k[u] + k[i]) * (abs(pos[u][0] - pos[i][0]) + abs(pos[u][1] - pos[i][1]))
        if con_cost < c[i]:
            c[i] = con_cost
            parent[i] = u
print(ans)
print(len(plants))
for p in sorted(plants):
    print(p + 1, end=' ')
print('')
print(len(connections))
for con in connections:
    print(con[0] + 1, con[1] + 1)
