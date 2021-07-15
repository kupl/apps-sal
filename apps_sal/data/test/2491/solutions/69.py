import sys

N, M = map(int,input().split())
es = []
for _ in range(M):
    e = list(map(int,input().split()))
    e[2] *= -1
    es.append(e)

INF = float('inf')
d = [INF for _ in range(N+1)]
d[1] = 0
negative = [0 for _ in range(N+1)]
for i in range(N):
    for j in range(M):
        e = es[j]
        if d[e[1]] > d[e[0]] + e[2]:
            d[e[1]] = d[e[0]] + e[2]
            if i == N-1:
                negative[e[0]] = 1
                negative[e[1]] = 1
for i in range(M):
    e = es[i]
    if negative[e[0]]:
        negative[e[1]] = 1
if negative[N]:
    print('inf')
else:
    print(-d[N])
