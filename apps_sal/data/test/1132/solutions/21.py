def bus_topology(neigh):
    single_neighbors = 0
    for i in range(1, len(neigh)):
        if len(neigh[i]) == 1:
            single_neighbors += 1
        elif len(neigh[i]) > 2:
            return False

    if single_neighbors == 2:
        return True
    else:
        return False


def ring_topology(neigh):
    for i in range(1, len(neigh)):
        if len(neigh[i]) > 2:
            return False
    return True


def star_topology(neigh, n):
    centernode = 0
    for i in range(1, len(neigh)):
        if len(neigh[i]) == n - 1:
            centernode += 1
        elif len(neigh[i]) != 1:
            return False

    if centernode == 1:
        return True
    else:
        return False


n, m = [int(x) for x in input().split()]
neighbors = [[] for x in range(n + 1)]

for i in range(m):
    u, v = (int(x) for x in input().split())
    neighbors[u].append(v)
    neighbors[v].append(u)


if bus_topology(neighbors):
    print("bus topology")
elif ring_topology(neighbors):
    print("ring topology")
elif star_topology(neighbors, n):
    print("star topology")
else:
    print("unknown topology")
