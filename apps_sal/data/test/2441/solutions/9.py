from sys import stdin


def main():
    n = int(input())
    costs = list(map(int, input().split()))
    input()
    chlds, prnts = [[] for _ in range(n)], [[] for _ in range(n)]
    for total in stdin.read().splitlines():
        u, v = list(map(int, total.split()))
        chlds[u - 1].append(v - 1)
        prnts[v - 1].append(u - 1)
    total, ways, childless, orphans = sum(costs), 1, [], []
    for i, cc, pp in zip(list(range(n)), chlds, prnts):
        if not (cc or pp):
            costs[i] = 0
        elif not cc:
            childless.append(i)
        elif not pp:
            orphans.append(i)
    while childless:
        u = childless.pop()
        costs[u] = 0
        for v in prnts[u]:
            chlds[v].remove(u)
            if not chlds[v]:
                childless.append(v)
    while orphans:
        u = orphans.pop()
        costs[u] = 0
        for v in chlds[u]:
            prnts[v].remove(u)
            if not prnts[v]:
                orphans.append(v)
    total -= sum(costs)
    pool = {u for u in range(n) if prnts[u] and chlds[u]}
    while pool:
        u = pool.pop()
        pp = prnts[u]
        cost, cnt = costs[u], 1
        while pp:
            u = pp.pop()
            if u in pool:
                pool.remove(u)
                pp += prnts[u]
                if costs[u] == cost:
                    cnt += 1
                elif costs[u] < cost:
                    cost, cnt = costs[u], 1
        total += cost
        ways = (ways * cnt) % 1000000007
    print(total, ways)


def __starting_point():
    main()


__starting_point()
