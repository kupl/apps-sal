n = int(input())
edge = [[] for _ in range(n)]
costs = [[] for _ in range(3)]
for i in range(3):
    costs[i] = [int(item) for item in input().split()]
for i in range(n - 1):
    u, v = [int(item) - 1 for item in input().split()]
    edge[u].append(v)
    edge[v].append(u)

beggining = None
for i, e in enumerate(edge):
    l = len(e)
    if l > 2:
        print(-1)
        return
    elif beggining is None and l == 1:
        beggining = i

place = []
visited = [0] * n
node = beggining
while node != -1:
    place.append(node)
    visited[node] = 1
    ok = False
    for v in edge[node]:
        if visited[v]:
            continue
        node = v
        ok = True
    if not ok:
        break

c_ans = [0] * n
color = [0] * n
ans = 10 ** 18
for init_c in range(3):
    ret = 0
    c = init_c
    for item in place:
        ret += costs[c][item]
        color[item] = c + 1
        c = (c + 1) % 3
    if ret < ans:
        ans = ret
        c_ans = color[:]
for init_c in range(3):
    ret = 0
    c = init_c
    for item in place:
        ret += costs[c][item]
        color[item] = c + 1
        c = (c + 2) % 3
    if ret < ans:
        ans = ret
        c_ans = color[:]

print(ans)
print(" ".join([str(item) for item in c_ans]))
