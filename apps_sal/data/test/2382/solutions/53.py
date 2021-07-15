from collections import Counter
from heapq import heappop, heappush


def solve(n, sss):
    ccc = Counter(sss)
    keys = sorted(list(ccc.keys()), reverse=True)
    if ccc[keys[0]] != 1:
        return False

    q = [(1, keys[0])]
    for k in keys[1:]:
        nq = []
        for _ in range(ccc[k]):
            try:
                r, s = heappop(q)
            except IndexError:
                return False
            if r < n:
                nq.append((r + 1, k))
                heappush(q, (r + 1, s))
        for item in nq:
            heappush(q, item)

    return True


n = int(input())
sss = list(map(int, input().split()))
print(('Yes' if solve(n, sss) else 'No'))

