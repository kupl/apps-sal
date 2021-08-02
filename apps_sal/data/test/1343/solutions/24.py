n, m, k = [int(x) for x in input().split()]
distance = {}
edge = {}
for i in range(1, n + 1):
    edge[i] = []
    distance[i] = -1
for i in range(1, m + 1):
    u, v, l = [int(x) for x in input().split()]
    edge[u].append((v, {'nei': v, 'dis': l}))
    edge[v].append((u, {'nei': u, 'dis': l}))
if(k != 0):
    a = [int(x) for x in input().split()]
    for z in a:
        distance[z] = 0
    for uu in a:
        frontier = [uu]
        while frontier:
            next = []
            for u in frontier:
                for (v, vv) in edge[u]:
                    jarak = vv.get('dis')
                    if (distance[v] == -1):
                        distance[v] = jarak + distance[u]
                        next.append(v)
                    else:
                        if(jarak + distance[u] < distance[v]):
                            next.append(v)
                            distance[v] = jarak + distance[u]
            frontier = next
    minim = 1000000000
    cek = False
    for uu in distance:
        if(distance[uu] != -1 and distance[uu] != 0):
            minim = min(minim, distance[uu])
            cek = True
    if cek:
        print(minim)
    else:
        print(-1)
else:
    print(-1)
