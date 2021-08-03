import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    # graph[b-1].append(a-1)
S, T = map(int, input().split())
S -= 1
T -= 1

D = [[-1] * 3 for _ in range(N)]
D[S][0] = 0
q = [(S, 0)]
while q:
    qq = []
    for p, d in q:
        for np in graph[p]:
            nd = (d + 1) % 3
            if D[np][nd] == -1:
                D[np][nd] = D[p][d] + 1
                qq.append((np, nd))
    q = qq

if D[T][0] == -1:
    print(-1)
else:
    print(D[T][0] // 3)
