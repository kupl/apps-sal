from collections import deque
from sys import maxsize as INT_MAX
n = int(input())
linea = input()
sep = linea.split()
nodos = list(map(int, sep))
conexiones = [list() for i in range(n)]
lista_bits = [list() for i in range(64)]
j = 0
for caquita in nodos:
    if caquita != 0:
        for z in range(64):
            if not caquita >> z:
                break
            bit = caquita >> z & 1
            if bit == 1:
                lista_bits[z].append(j)
    else:
        j -= 1
        n -= 1
    j += 1
gr = conexiones


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


al_menos_tres = False
son_2 = False
for listita in lista_bits:
    if len(listita) >= 3:
        al_menos_tres = True
        break
    elif len(listita) == 2:
        son_2 = True
        x = listita[0]
        y = listita[1]
        gr[x].append(y)
        gr[y].append(x)
if al_menos_tres:
    print(3)
elif not son_2:
    print(-1)
else:
    print(shortest_cycle(n))
