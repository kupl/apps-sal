from sys import maxsize as INT_MAX
from collections import deque
n = int(input())
linea = input()
sep = linea.split()
nodos = list(map(int, sep))
bits = [list() for i in range(64)]
j = 0
for s in nodos:
    if s != 0:
        for i in range(64):
            bit = s >> i & 1
            if bit == 1:
                bits[i].append(j)
    else:
        j -= 1
        n -= 1
    j += 1
dos = False
ejecucion = True
gr = [list() for i in range(n)]
for k in bits:
    if len(k) == 2:
        dos = True
        x = k[0]
        y = k[1]
        gr[x].append(y)
        gr[y].append(x)
    elif len(k) >= 3:
        ejecucion = False
        break
if ejecucion == False:
    print(3)
elif not dos:
    print(-1)
else:

    def shortest_cycle(n: int) -> int:
        ans = INT_MAX
        for i in range(n):
            dist = [int(1000000000.0)] * n
            par = [-1] * n
            dist[i] = 0
            q = deque()
            q.append(i)
            while q:
                x = q[0]
                q.popleft()
                for child in gr[x]:
                    if dist[child] == int(1000000000.0):
                        dist[child] = 1 + dist[x]
                        par[child] = x
                        q.append(child)
                    elif par[x] != child and par[child] != x:
                        ans = min(ans, dist[x] + dist[child] + 1)
        if ans == INT_MAX:
            return -1
        else:
            return ans
    print(shortest_cycle(n))
