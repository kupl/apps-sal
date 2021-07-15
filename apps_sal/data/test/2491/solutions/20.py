N, M = map(int, input().split())
edges = []
E = [[] for _ in range(N)]

for _ in range(M):
    fr, to, cost = map(int, input().split())
    fr -= 1
    to -= 1
    edges.append((fr, to, -cost))
    E[to].append(fr)

def canGo():
    st = [N - 1]
    visited = [False] * N
    visited[N - 1] = True
    while st:
        for to in E[st.pop()]:
            if visited[to]:
                continue
            visited[to] = True
            st.append(to)
    return visited

V = canGo()

minDist = [float('inf')] * N
minDist[0] = 0

for i in range(N + 1):
    for fr, to, cost in edges:
        d = minDist[fr] + cost
        if minDist[to] > d:
            if i == N and V[to]:
                print('inf')
                return
            minDist[to] = d

print(-minDist[N - 1])
