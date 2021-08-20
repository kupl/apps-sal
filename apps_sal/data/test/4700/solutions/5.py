(n, m) = [int(i) for i in input().split()]
h = [int(i) for i in input().split()]
edges = [[] for i in range(n)]
for _ in range(m):
    edge = [int(i) - 1 for i in input().split()]
    edges[edge[0]].append(edge[1])
    edges[edge[1]].append(edge[0])
cnt = 0
for i in range(n):
    flg = True
    for j in edges[i]:
        if h[i] <= h[j]:
            flg = False
            break
    if flg:
        cnt += 1
print(cnt)
