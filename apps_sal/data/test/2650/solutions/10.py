def solve():
    from heapq import heappop, heappush
    from collections import defaultdict
    (n, q) = list(map(int, input().split()))
    rates = [0] * (n + 1)
    belong = [0] * (n + 1)
    en = [[] for _ in range(2 * 10 ** 5 + 1)]
    ob = [defaultdict(int) for _ in range(2 * 10 ** 5 + 1)]
    res = []
    res_gone = defaultdict(int)
    ans = []
    for i in range(1, n + 1):
        (a, b) = list(map(int, input().split()))
        rates[i] = a
        belong[i] = b
        heappush(en[b], -a)
    for e in en:
        if e:
            x = -heappop(e)
            heappush(res, x)
            heappush(e, -x)
    for i in range(q):
        (c, d) = list(map(int, input().split()))
        tmp = belong[c]
        obr = rates[c]
        ob[tmp][obr] += 1
        ox_s = -heappop(en[tmp])
        res_gone[ox_s] += 1
        heappush(en[tmp], -ox_s)
        if en[d]:
            ox_m = -heappop(en[d])
            res_gone[ox_m] += 1
            heappush(en[d], -ox_m)
        belong[c] = d
        heappush(en[d], -rates[c])
        nx_s = -heappop(en[tmp])
        while ob[tmp][nx_s] != 0:
            ob[tmp][nx_s] -= 1
            nx_s = -heappop(en[tmp]) if en[tmp] else 0
        if nx_s != 0:
            heappush(res, nx_s)
            heappush(en[tmp], -nx_s)
        nx_m = -heappop(en[d])
        heappush(res, nx_m)
        heappush(en[d], -nx_m)
        fair = heappop(res)
        while res_gone[fair] != 0:
            res_gone[fair] -= 1
            fair = heappop(res)
        ans.append(fair)
        heappush(res, fair)
    print('\n'.join(map(str, ans)))


solve()
