from collections import defaultdict
from sys import stdin
input = stdin.readline


class N:

    def __init__(self, c) -> None:
        self.c = c
        self.ch = []


def __starting_point():
    (n, m) = list(map(int, input().split()))
    carr = list(map(int, input().split()))
    arr = [N(x) for x in carr]
    for _ in range(m):
        (a, b) = list(map(int, input().split()))
        arr[a - 1].ch.append(arr[b - 1])
        arr[b - 1].ch.append(arr[a - 1])
    for x in arr:
        x.ch = list([y for y in x.ch if y.c != x.c])
    dct = defaultdict(lambda: set())
    for x in arr:
        for y in x.ch:
            if y.c != x.c:
                dct[x.c].add(y.c)
    narr = []
    for (key, value) in list(dct.items()):
        narr.append((key, len(value)))
    narr.sort(key=lambda x: x[1], reverse=True)
    if narr:
        narr = list(sorted([x for x in narr if x[1] == narr[0][1]], key=lambda x: x[0]))
        print(narr[0][0])
    else:
        print(min(carr))


__starting_point()
