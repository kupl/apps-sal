import sys
from io import StringIO


def main():
    def find_set(v):
        tmp = []
        while v != parent[v]:
            tmp.append(v)
            v = parent[v]
        for i in tmp:
            parent[i] = v

        return v

    sys.stdin = StringIO(sys.stdin.read())
    input = lambda: sys.stdin.readline().rstrip('\r\n')

    n, m = list(map(int, input().split(' ')))
    a = list(map(int, input().split(' ')))

    edges = []
    for _ in range(m):
        x, y, w = list(map(int, input().split(' ')))
        edges.append((x - 1, y - 1, w))

    min_val = min(a)
    min_ind = a.index(min_val)

    for i in range(n):
        edges.append((min_ind, i, min_val + a[i]))

    parent, rank = list(range(n)), [0] * n
    cost = 0

    for edge in sorted(edges, key=lambda edge: edge[2]):
        find_u, find_v = find_set(edge[0]), find_set(edge[1])

        if find_u != find_v:
            cost += edge[2]

            if rank[find_u] < rank[find_v]:
                find_v, find_u = find_u, find_v
            elif rank[find_u] == rank[find_v]:
                rank[find_u] += 1

            parent[find_v] = find_u

    print(cost)


main()
