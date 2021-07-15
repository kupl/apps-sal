def main():
    n, m = list(map(int, input().split()))
    nm = n * m
    neigh = [[] for _ in range(nm)]
    for i in range(0, nm - m, m):
        for j in range(i, i + m):
            neigh[j].append(j + m)
            neigh[j + m].append(j)
    for i in range(0, nm, m):
        for j in range(i, i + m - 1):
            neigh[j].append(j + 1)
            neigh[j + 1].append(j)
    field = [c == '.' for _ in range(n) for c in input()]
    l = []
    for _ in (0, 1):
        i, j = list(map(int, input().split()))
        l.append(i * m + j - m - 1)
    start, stop = l
    if start == stop:
        print(("NO", "YES")[any(field[_] for _ in neigh[stop])])
        return
    field[start] = True
    if field[stop] and sum(field[_] for _ in neigh[stop]) < 2:
        print("NO")
        return
    nxt, field[stop] = (start,), True
    while nxt:
        cur, nxt = nxt, []
        for u in cur:
            if u == stop:
                print("YES")
                return
            for v in neigh[u]:
                if field[v]:
                    field[v] = False
                    nxt.append(v)
    print("NO")


def __starting_point():
    main()

__starting_point()
