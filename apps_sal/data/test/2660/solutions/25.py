import heapq as hq
Q = int(input())
minval = 0
argminval = -10 ** 9
(L, R) = ([10 ** 9], [10 ** 9])
(lenL, lenR) = (0, 0)
for _ in range(Q):
    qi = list(map(int, input().split()))
    if qi[0] == 1:
        (ai, bi) = (qi[1], qi[2])
        (LC, RC) = (-1 * L[0], R[0])
        if lenL == lenR:
            if ai < RC:
                hq.heappush(L, -1 * ai)
            else:
                hq.heappop(R)
                hq.heappush(L, -1 * RC)
                hq.heappush(R, ai)
            lenL += 1
            argminval = -1 * L[0]
            minval += abs(argminval - ai) + bi
        else:
            if ai < LC:
                hq.heappop(L)
                hq.heappush(L, -1 * ai)
                hq.heappush(R, LC)
            else:
                hq.heappush(R, ai)
            lenR += 1
            minval += abs(argminval - ai) + bi
            argminval = -1 * L[0]
    else:
        print('{} {}'.format(argminval, minval))
