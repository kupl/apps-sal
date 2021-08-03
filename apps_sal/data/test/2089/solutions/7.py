from array import array
n, m, s, t = list(map(int, input().split()))
neighbours = [array('H', [])]
neighbours.clear()
neighbours.append(0)
neighbours.extend((array('H', []) for _ in range(n)))
for __ in range(m):
    u, v = list(map(int, input().split()))
    neighbours[u].append(v)
    neighbours[v].append(u)
dist1 = array('H', [0] * (n + 1))
visit = array('B', [0] + [1] * n)
queue = array('H', [s])
dists = array('H', [0])
index = 0
while index < len(queue):
    qi = queue[index]
    if visit[qi]:
        visit[qi] = 0
        di = dists[index]
        dist1[qi] = di
        for oth in neighbours[qi]:
            queue.append(oth)
            dists.append(di + 1)
    index += 1
dist2 = array('h', [0] * (n + 1))
visit = array('B', [0] + [1] * n)
queue = array('h', [t])
dists = array('h', [dist1[t]])
index = 0
while index < len(queue):
    qi = queue[index]
    if visit[qi]:
        visit[qi] = 0
        di = dists[index]
        dist2[qi] = di
        for oth in neighbours[qi]:
            queue.append(oth)
            dists.append(di - 1)
    index += 1
res = 0
for s in range(1, n + 1):
    for t in range(1, s):
        if (s not in neighbours[t]) and (dist1[s] + 1 >= dist2[t]) and (dist1[t] + 1 >= dist2[s]):
            res += 1
print(res)
