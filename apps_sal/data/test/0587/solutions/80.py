import sys
from collections import deque
from heapq import heappop, heappush

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = list(map(int, input().split()))
    TD = [list(map(int, input().split())) for _ in range(n)]
    TD.sort(key=lambda z: -z[1])
    TD_new = [[] for _ in range(n)]
    for t, d in TD:
        TD_new[t - 1].append([d, 0] if len(TD_new[t - 1]) else [d, 1])

    ALL = []
    for td in TD_new:
        ALL.extend(td)
    ALL.sort(reverse=True)
    que = deque(ALL)

    x = y = 0
    zero = []
    for _ in range(k):
        d, ex = que.popleft()
        x += d
        y += ex
        if ex == 0:
            heappush(zero, d)

    res = x + y ** 2
    while que:
        d, ex = que.popleft()
        if ex:
            if zero:
                x += d - heappop(zero)
                y += 1
                res = max(res, x + y ** 2)
            else:
                break

    print(res)


def __starting_point():
    resolve()

__starting_point()
