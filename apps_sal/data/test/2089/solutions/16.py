def get_amount_variants(routes, n, s, t):
    """
    :param List[List[int]] routes:
    :param int n:
    :param int s:
    :param int t:
    :return: int
    """
    connects = [[] for _ in range(n + 1)]
    for st, end in routes:
        connects[st].append(end)
        connects[end].append(st)

    w_h = get_shortest_ways(connects, s)
    w_j = get_shortest_ways(connects, t)
    amount = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if min(w_h[i] + w_j[j], w_h[j] + w_j[i]) + 1 >= w_h[t] and i not in connects[j]:
                amount += 1
    return amount


def get_shortest_ways(connects, st):
    res = [int(1e9) if _ != st else 0 for _ in range(len(connects) + 1)]
    available = [(x, 0) for x in connects[st]]
    while len(available) > 0:
        point, weight = available.pop(0)
        if res[point] != 0 and res[point] < weight + 1:
            continue

        res[point] = weight + 1
        available += [(x, weight + 1) for x in connects[point] if res[x] == int(1e9) and x != st]
    return res


n, m, s, t = map(int, input().strip().split())
routes = []
for i in range(m):
    routes.append(map(int, input().split()))
print(get_amount_variants(routes, n, s, t))
