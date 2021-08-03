n, m = map(int, input().split())
edge = [[] for _ in range(n)]
for i in range(m):
    x, y = map(int, input().split())
    edge[x - 1].append(y - 1)
    edge[y - 1].append(x - 1)
for i in edge[0]:
    if n - 1 in edge[i]:
        print("POSSIBLE")
        return
print("IMPOSSIBLE")
