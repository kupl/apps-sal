from sys import stdin


def main():
    (n, costs) = (int(input()), list(map(int, input().split())))
    input()
    (chlds, prnts) = ([[] for _ in range(n)], [[] for _ in range(n)])
    for total in stdin.read().splitlines():
        (u, v) = list(map(int, total.split()))
        chlds[u - 1].append(v - 1)
        prnts[v - 1].append(u - 1)
    (avail, order) = ([True] * n, [])
    for (u, f) in enumerate(avail):
        if f:
            (avail[u], stack) = (False, [u, prnts[u]])
            while stack:
                while stack[-1]:
                    u = stack[-1].pop()
                    if avail[u]:
                        avail[u] = False
                        stack.append(u)
                        stack.append(prnts[u])
                del stack[-1]
                order.append(stack.pop())
    (avail, res, cnt, ways) = ([True] * n, 0, 0, 1)
    while order:
        u = order.pop()
        if avail[u]:
            (avail[u], stack, cst, cnt) = (False, chlds[u], costs[u], 0)
            while stack:
                u = stack.pop()
                if avail[u]:
                    avail[u] = False
                    if cst > costs[u]:
                        (cst, cnt) = (costs[u], 0)
                    elif cst == costs[u]:
                        cnt += 1
                    stack += chlds[u]
            res += cst
            if cnt:
                ways = ways * (cnt + 1) % 1000000007
    print(res, ways)


def __starting_point():
    main()


__starting_point()
