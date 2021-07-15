from collections import deque
from sys import stdin, stdout
input = stdin.readline

 
saida = []
t = int(input())
modulo = 998244353

for _ in range(t):
    ans = 1
    part = 0
    factor = 0
    queue = deque([])
    n, m = map(int, input().split())
    if m > (n // 2) * ( n // 2 + 1):
        saida.append('0')
        for edge_count in range(m):
            input()
        continue
    edge = [[] for i in range(n + 1)]
    visitados = [-1] * (n + 1)
    assure = 1
 
    for edge_count in range(m):
        u, v = map(int, input().split())
        edge[u].append(v)
        edge[v].append(u)
    visitados[1] = 0
    queue.append(1)
 
    break_all = False
    while not break_all:
        even, odd = 1, 0
        while queue and not break_all:
            search = queue.popleft()
            
            current = visitados[search]
            for i in edge[search]:
                if visitados[i] == -1:
                    visitados[i] = current ^ 1
                    if visitados[i] & 1:
                        odd += 1
                    else:
                        even += 1
                    queue.append(i)
                elif visitados[i] == current:
                    break_all = True
                else:
                    assert visitados[i] == current ^ 1
        if break_all:
            ans = 0
        else:
            if (even, odd) == (1, 0):
                factor += 1
            else:
                ans *= pow(2, even, modulo) + pow(2, odd, modulo)
                ans %= modulo
        while assure <= n:
            if visitados[assure] == -1:
                part += 1
                visitados[assure] = 2 * part
 
                queue.append(assure)
                break
            assure += 1
        if assure == n + 1:
            break
    ans *= pow(3, factor, modulo)
    ans %= modulo
    saida.append(str(ans))
print('\n'.join(saida))
