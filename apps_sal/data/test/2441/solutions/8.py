from sys import stdin


def main():
    n = int(input())
    costs = list(map(int, input().split()))
    input()
    (chlds, prnts) = ([[] for _ in range(n)], [[] for _ in range(n)])
    for total in stdin.read().splitlines():
        (u, v) = list(map(int, total.split()))
        chlds[u - 1].append(v - 1)
        prnts[v - 1].append(u - 1)
    (total, ways, pool) = (0, 1, {i for i in range(n) if not (prnts[i] and chlds[i])})
    while pool:
        u = pool.pop()
        total += costs[u]
        for v in prnts[u]:
            chlds[v].remove(u)
            if not chlds[v]:
                pool.add(v)
        for v in chlds[u]:
            prnts[v].remove(u)
            if not prnts[v]:
                pool.add(v)
    pool = {u for u in range(n) if prnts[u] and chlds[u]}
    while pool:
        u = pool.pop()
        pp = prnts[u]
        (cost, cnt) = (costs[u], 1)
        while pp:
            u = pp.pop()
            if u in pool:
                pool.remove(u)
                pp += prnts[u]
                if costs[u] == cost:
                    cnt += 1
                elif costs[u] < cost:
                    (cost, cnt) = (costs[u], 1)
        total += cost
        ways = ways * cnt % 1000000007
    print(total, ways)


def __starting_point():
    main()


__starting_point()
