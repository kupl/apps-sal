

import collections


def sol(lst):
    d = collections.defaultdict(list)
    for i, x in enumerate(lst):
        d[x].append(i)

    MIN_SOL = 10**10
    for x in d:
        for a, b in zip(d[x], d[x][1:]):
            MIN_SOL = min(MIN_SOL, b - a + 1)
    if MIN_SOL == 10**10:
        print(-1)
    else:
        print(MIN_SOL)


t = int(input())
for _ in range(t):
    _ = int(input())
    sol([int(x) for x in input().split()])
