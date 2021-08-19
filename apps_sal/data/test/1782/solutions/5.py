import sys


def solve():
    (n, k) = map(int, input().split())
    if n // k < 3 or n < 6:
        print(-1)
        return
    res = list()
    for i in range(1, k + 1):
        res.append(i)
        res.append(i)
    for i in range(1, k + 1):
        res.append(i)
    while len(res) < n:
        res.append(1)
    print(' '.join(map(str, res)))


solve()
