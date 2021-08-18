
m, k = map(int, input().split())
g = dict()
for edge_i in range(m):
    a, b = map(int, input().split())
    if a not in g:
        g[a] = set()
    if b not in g:
        g[b] = set()
    g[a].add(b)
    g[b].add(a)

for x in sorted(g.keys()):
    prob = []
    friends = g[x]
    for y in g:
        if y in friends or y == x:
            continue
        inter = g[y] & friends
        if len(inter) * 100 >= k * len(friends):
            prob.append(y)
    print(x, ": ", len(prob), end=' ', sep='')
    for elem in sorted(prob):
        print(elem, end=' ')
    print()
