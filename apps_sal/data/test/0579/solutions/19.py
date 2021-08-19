from collections import Counter
from heapq import heapify, heappop, heappush
from itertools import accumulate


def solve(n, k, ppp, ccc):
    NINF = -10 ** 18
    ans = NINF
    checked = [False] * n
    for s in range(n):
        if checked[s] == True:
            continue
        checked[s] = True
        scores = [ccc[ppp[s]]]
        v = ppp[s]
        while v != s:
            scores.append(ccc[ppp[v]])
            checked[v] = True
            v = ppp[v]
        l = len(scores)
        (d, m) = divmod(k, l)
        loop = sum(scores)
        if d > 0:
            d -= 1
            m += l
        scores += scores * 2
        scores.insert(0, 0)
        acc = list(accumulate(scores))
        base = max(0, loop * d)
        range_max = [-a for a in acc[1:m + 1]]
        available_max = Counter(range_max)
        heapify(range_max)
        for i in range(l):
            while available_max[range_max[0]] == 0:
                heappop(range_max)
            ans = max(ans, base - range_max[0] - acc[i])
            old = -acc[i + 1]
            new = -acc[i + m + 1]
            available_max[old] -= 1
            available_max[new] += 1
            heappush(range_max, new)
    return ans


(n, k) = list(map(int, input().split()))
ppp = list(map(int, input().split()))
ppp = [p - 1 for p in ppp]
ccc = list(map(int, input().split()))
print(solve(n, k, ppp, ccc))
