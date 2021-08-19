import itertools
(n, m) = list(map(int, input().split()))
routes = list(itertools.permutations([i for i in range(2, n + 1)]))
nodes = {}
ans = 0
for i in range(1, n + 1):
    nodes[i] = []
for _ in range(m):
    (a, b) = list(map(int, input().split()))
    nodes[a].append(b)
    nodes[b].append(a)
for i in range(len(routes)):
    jud = 1
    if routes[i][0] not in nodes[1]:
        jud = 0
    for j in range(n - 2):
        if routes[i][j + 1] not in nodes[routes[i][j]]:
            jud = 0
    ans += jud
print(ans)
