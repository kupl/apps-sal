import sys
from heapq import heappush, heappop

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = list(map(int, input().split()))
    AB = [[] for _ in range(m)]
    for _ in range(n):
        a, b = list(map(int, input().split()))
        if a <= m:
            AB[m - a].append(b)

    que = []
    res = 0
    for i in reversed(list(range(m))):
        for b in AB[i]:
            heappush(que, -b)
        if que:
            res += heappop(que) * -1
    print(res)


def __starting_point():
    resolve()


__starting_point()
