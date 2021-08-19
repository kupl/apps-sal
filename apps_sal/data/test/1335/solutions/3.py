from math import trunc
from collections import defaultdict, deque


def round(x):
    return trunc(x + 0.5)


def main():
    (n, k) = list(map(int, input().split()))
    an = list(map(int, input().split()))
    ts = [0] * (16 * 10 ** 5)
    ts[0] = k
    ds = [0] * (16 * 10 ** 5)
    m = -k
    ready = defaultdict(list)
    sol = [0] * n
    q = deque(list(range(n)))
    for i in range(len(ts)):
        free = ts[i]
        m += free
        ds[i] = round(100 * m / n)
        j = 0
        while q and j < free:
            si = q.popleft()
            ts[i + an[si]] += 1
            sol[si] = i
            j += 1
        if m == n:
            break
    res = 0
    for i in range(n):
        t = sol[i]
        for q in range(an[i]):
            if ds[t + q] == q + 1:
                res += 1
                break
    print(res)


main()
