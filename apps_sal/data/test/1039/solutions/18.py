N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N - 1):
    (a, b, c) = list(map(int, input().split()))
    graph[a - 1].append((b - 1, c))
    graph[b - 1].append((a - 1, c))
(Q, K) = list(map(int, input().split()))
K -= 1
query = [tuple((int(x) for x in input().split())) for _ in range(Q)]
seen = {K}
v = [K]
distfromK = [0] * N
while len(v) != 0:
    for nv in graph[v[0]]:
        if nv[0] in seen:
            continue
        distfromK[nv[0]] = distfromK[v[0]] + nv[1]
        v.append(nv[0])
        seen.add(nv[0])
    v.pop(0)
for q in query:
    print(distfromK[q[0] - 1] + distfromK[q[1] - 1])
