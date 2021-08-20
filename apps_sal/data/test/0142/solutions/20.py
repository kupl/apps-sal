INF = int(1e+18)


def read_int():
    return list(map(int, input().split()))


(n, l) = read_int()
costs = read_int()
bottles = [(1 << i, c) for (i, c) in enumerate(costs)]
bottles.sort(key=lambda b: (b[1] / b[0], 1 / b[1]))
min_cost = dict()


def find_min_cost(l):
    if l == 0:
        return 0
    if l in min_cost:
        return min_cost[l]
    c = INF
    for b in bottles:
        c1 = (l + b[0] - 1) // b[0] * b[1]
        c2 = l // b[0] * b[1] + find_min_cost(l % b[0]) if l > b[0] else INF
        c = min(c, c1, c2)
    min_cost[l] = c
    return min_cost[l]


print(find_min_cost(l))
