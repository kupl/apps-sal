n, m = [int(x) for x in input().split()]
edge = {}
for i in range(1, n + 1):
    edge[i] = {}
    for j in range(1, m + 1):
        edge[i][j] = []
for i in range(m):
    a, b, c = [int(x) for x in input().split()]
    edge[a][c].append(b)
    edge[b][c].append(a)
q = int(input())
for i in range(q):
    u, v = [int(x) for x in input().split()]
    count = 0
    for key in edge[u]:
        level = {u: 0}
        frontier = [u]
        found = False
        while frontier and not found:
            next = []
            for uu in frontier:
                for vv in edge[uu][key]:
                    if not(vv in level):
                        if vv == v:
                            found = True
                        level[vv] = 0
                        next.append(vv)
            frontier = next
        if(found):
            count += 1
    print(count)
