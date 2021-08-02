N, M = map(int, input().split())
G = [[] for _ in range(N)]

for i in range(M):
    x, y, z = map(int, input().split())
    G[x - 1].append(y - 1)
    G[y - 1].append(x - 1)

lst = []
visited = [0] * N
for i in range(N):
    if visited[i] == 1: continue
    temp = [i]
    lst1 = [i]
    visited[i] = 1
    while temp:
        p = temp.pop()
        for q in G[p]:
            if visited[q] == 0:
                visited[q] = 1
                lst1.append(q)
                temp.append(q)
    if lst1 != []: lst.append(lst1)

print(len(lst))
