n = int(input())
d = {}
sees = []
for _ in range(n):
    a, b = map(int, input().split())
    if a not in d:
        d[a] = set()
    if b not in d:
        d[b] = set()
    d[a].add(b)
    d[b].add(a)
    sees.append(set((a, b)))
res = []
if b in sees[a - 1]:
    res.extend([a, b])
    d[b].remove(a)
else:
    res.extend([b, a])
    d[a].remove(b)
for _ in range(n - 2):
    last = res[-1]
    nex = d[last].pop()
    d[nex].remove(last)
    res.append(nex)
for r in res:
    print(r, end=' ')
print()
