def R(): return map(int, input().split())


n = int(input())
degs, xors = [0] * (2 ** 16 + 1), [0] * (2 ** 16 + 1)
edges = []
for curr in range(n):
    degs[curr], xors[curr] = R()
q = []
for curr in range(n):
    if degs[curr] == 1:
        q.append(curr)
while q:
    curr = q.pop()
    if degs[curr] != 1:
        continue
    neighbor = xors[curr]
    edges.append((min(curr, neighbor), max(curr, neighbor)))
    degs[neighbor] -= 1
    xors[neighbor] ^= curr
    if degs[neighbor] == 1:
        q.append(neighbor)
filter(lambda p: p[0] < p[1], edges)
print(len(edges))
for u, v in edges:
    if u < v:
        print(u, v)
