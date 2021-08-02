n, m = map(int, input().split())
edge = []
for i in range(m):
    a, b, c = map(int, input().split())
    edge.append([a, b, -c])
check = [False for i in range(n + 1)]
inf = False
node = [float('inf') for i in range(n + 1)]
node[1] = 0
for i in range(n - 1):
    for s, e, c in edge:
        if node[e] > node[s] + c:
            node[e] = node[s] + c
for i in range(n):
    for s, e, c in edge:
        if node[e] > node[s] + c:
            node[e] = node[s] + c
            check[e] = True
        if check[s]:
            check[e] = True
if check[-1]:
    print('inf')
else:
    print(-node[-1])
