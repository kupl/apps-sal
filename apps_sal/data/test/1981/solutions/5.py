
import math
import sys
sys.setrecursionlimit(10**6)
n, m = list(map(int, input().split()))
cats = list(map(int, input().split()))
G = [[] for i in range(n)]

for i in range(n - 1):
    x, y = [int(x) - 1 for x in input().split()]
    G[x].append(y)
    G[y].append(x)

q = []
q.append((0, -1, 0, 0))
count = 0
while q != []:
    u, parent, consecutive, cat_num = q.pop()

    if not cats[u]:
        consecutive = 0
    consecutive += cats[u]
    cat_num = max(consecutive, cat_num)
    if cat_num <= m and len(G[u]) == 1 and u != 0:
        count += 1

    for v in G[u]:
        if v != parent:
            q.append((v, u, consecutive, cat_num))
print(count)
