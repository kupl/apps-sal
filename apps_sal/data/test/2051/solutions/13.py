n, m, k = list(map(int, input().split()))
socks = list(map(int, input().split()))
adj = [[] for _ in range(n)]
for _ in range(m):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    adj[a].append(b)
    adj[b].append(a)

component = [None] * n
cur_comp = 0

for i in range(n):
    if component[i] is None:
        todo = [i]
        while todo:
            xi = todo.pop()
            component[xi] = cur_comp
            for neighbour in adj[xi]:
                if component[neighbour] is None:
                    todo.append(neighbour)
        cur_comp += 1

components = [[] for _ in range(cur_comp)]
for v, c in enumerate(component):
    components[c].append(v)

out = 0
for c in components:
    counter = {}
    for v in c:
        if socks[v] not in counter:
            counter[socks[v]] = 0
        counter[socks[v]] += 1
    out += len(c) - max(counter.values())
print(out)

