import collections
n, m = map(int, input().split())
rs = []
for i in range(m):
    u, v = map(int, input().split())
    rs.append((u - 1, v - 1))
d = dict()
for v in range(n):
    d[v] = set()
for r in rs:
    u = r[0]
    v = r[1]
    setU = d.get(u, set())
    setV = d.get(v, set())
    setU.add(v)
    setV.add(u)
    d[u] = setU
    d[v] = setV
seen = [False] * n
result = 0
for v in range(n):
    if seen[v]:
        continue
    good = True
    deq = collections.deque([v])
    while len(deq) > 0:
        currV = deq.pop()
        seen[currV] = True
        if len(d[currV]) != 2:
            good = False
        for u in d[currV]:
            if seen[u]:
                continue
            seen[u] = True
            deq.append(u)
    if good:
        result += 1
print(result)
