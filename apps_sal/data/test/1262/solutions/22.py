from sys import stdin, stdout
from collections import Counter
def ai(): return list(map(int, stdin.readline().split()))
def ei(): return map(int, stdin.readline().split())
def ip(): return int(stdin.readline().strip())
def op(ans): return stdout.write(str(ans) + '\n')


n = ip()
pos = [ai() for i in range(n)]
c = ai()
k = ai()

connections = []
plants = []
used = [False] * n
parent = [-1] * n

ans = 0
n_ = n
while n_:
    n_ -= 1
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
for i in sorted(plants):
    print(i + 1, end=' ')
print()
print(len(connections))
for i in connections:
    print(i[0] + 1, i[1] + 1)
