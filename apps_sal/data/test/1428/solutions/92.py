from itertools import combinations, permutations
3
# -*- coding:utf-8 -*-


def main():
    n, nc = list(map(int, input().split()))
    md = [list(map(int, input().split())) for _ in range(nc)]
    mc = [list([int(c) - 1 for c in input().split()]) for _ in range(n)]
    cnt_c = [[0] * nc for _ in range(3)]

    for i in range(n):
        for j in range(n):
            cnt_c[(i + j) % 3][mc[i][j]] += 1

    def calc_cost(lx, itarget):
        return sum([cnt * md[i][itarget] for i, cnt in enumerate(lx)])

    cost = 10**9
    for inds in combinations(list(range(nc)), 3):
        for itargets in permutations(inds):
            cost = min(cost, sum([calc_cost(cnt_c[i], itarget) for i, itarget in enumerate(itargets)]))
    print(cost)


def __starting_point():
    main()


__starting_point()
