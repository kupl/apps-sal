N, M = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
    ta, tb = map(int, input().split())
    E[ta - 1].append(tb - 1)
S, T = map(int, input().split())
S -= 1
T -= 1

INF = float('inf')
dist = [[INF] * N for _ in range(3)]
dist[0][S] = 0
q = [[S, 0]]

while q:
    cp, cd = q.pop(0)
    nd = (cd + 1) % 3
    for np in E[cp]:
        if dist[nd][np] != INF:
            continue
        else:
            dist[nd][np] = dist[cd][cp] + 1
            q.append([np, nd])

ans = dist[0][T]
if ans == INF:
    print(-1)
else:
    print(ans // 3)
