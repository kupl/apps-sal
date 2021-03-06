from heapq import heappop, heappush
import sys
sysread = sys.stdin.readline
read = sys.stdin.read
sys.setrecursionlimit(10 ** 7)


def sum_between(a, b):
    if a > b:
        (a, b) = (b, a)
    return (b - a + 1) * (b + a) // 2


def run():
    N = int(input())
    n_dots = 0
    for i in range(1, N + 1):
        n_dots += (1 + i) * i // 2
    ans = (N - 1) * (N + 1) * N // 2
    lr = list(map(int, read().split()))
    l = lr[::2]
    r = lr[1::2]
    for (l, r) in zip(l, r):
        if l > r:
            (l, r) = (r, l)
        tmp = 0
        if l > 1:
            tmp += sum_between(r - 1, r - l + 1)
        tmp += r - l
        tmp += sum_between(N - l, 1)
        ans -= tmp
    print(n_dots - ans)
    ans = (N - 1) * N * N


def __starting_point():
    run()


__starting_point()
