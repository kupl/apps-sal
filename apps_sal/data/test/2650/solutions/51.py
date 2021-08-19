from collections import defaultdict
import heapq
3
# -*- coding:utf-8 -*-


def remove(hq, belongs, maxs, pd):
    while hq:
        if belongs[hq[0][1]] != pd:
            heapq.heappop(hq)
        else:
            heapq.heappush(maxs, (-hq[0][0], hq[0][1], pd))
            break


def main():
    n, q = list(map(int, input().strip().split()))
    rates = defaultdict(list)
    id2rate = [0] * n
    belongs = [0] * n
    for i in range(n):
        a, b = list(map(int, input().strip().split()))
        b -= 1
        rates[b].append((-a, i))
        belongs[i] = b
        id2rate[i] = a

    maxs = []
    for k in list(rates.keys()):
        heapq.heapify(rates[k])
        maxs.append((-rates[k][0][0], rates[k][0][1], k))
    heapq.heapify(maxs)

    for _ in range(q):
        c, d = list(map(int, input().strip().split()))
        c -= 1
        d -= 1

        pd = belongs[c]
        belongs[c] = d
        remove(rates[pd], belongs, maxs, pd)

        heapq.heappush(rates[d], (-id2rate[c], c))
        remove(rates[d], belongs, maxs, d)
        heapq.heappush(maxs, (-rates[d][0][0], rates[d][0][1], d))

        while maxs:
            if belongs[maxs[0][1]] != maxs[0][2] or rates[maxs[0][2]][0][1] != maxs[0][1]:
                heapq.heappop(maxs)
            else:
                print((maxs[0][0]))
                break


def __starting_point():
    main()


__starting_point()
