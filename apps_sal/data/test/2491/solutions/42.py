def find_negative_loop(n, es, d):
    check = [0 for _ in range(n)]
    for _ in range(n):
        for p, q, r in es:
            if d[p] != float("inf") and d[q] > d[p] + r:
                d[q] = d[p] + r
                check[q] = True
            if check[p]:
                check[q] = True
    return check


def shortest_path(s, n, es):
    d = [float("inf")] * n
    d[s] = 0
    for _ in range(n):
        update = False
        for p, q, r in es:
            if d[p] != float("inf") and d[q] > d[p] + r:
                d[q] = d[p] + r
                update = True
        if not update:
            break
    return d


n, w = map(int, input().split())
es = []

for _ in range(w):
    x, y, z = map(int, input().split())
    es.append([x - 1, y - 1, -z])


d = shortest_path(0, n, es)


c = find_negative_loop(n, es, d)


if c[-1]:
    print("inf")
else:
    print(-d[-1])
