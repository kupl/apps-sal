N,M = list(map(int,input().split()))
from collections import deque
v = [deque([]) for _ in range(N)]

for i in range(M):
    a,b,c = list(map(int,input().split()))
    a,b = a-1,b-1
    v[a].append([b,c])
    v[b].append([a,c])

s = deque([])
for i in range(N):
    ls = [[-1,M*10000]]*N
    ls[i] =  [-1,0]
    q = [deque(j for j in k) for k in v]
    l = deque([i])
    while l:
        u = l.popleft()
        x = len(q[u])
        for i in range(x):
            e = q[u].popleft()
            if ls[u][1] + e[1] < ls[e[0]][1]:
                ls[e[0]] = [u, ls[u][1] + e[1]]
                l.append(e[0])
            q[u].append(e)
    for j,e in enumerate(ls):
        if e[0] != -1:
             s.append([min(j,e[0]),max(j,e[0])])

s = list(map(list, set(map(tuple, s))))
print((M-len(s)))

