import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def get_num_draw(n, x):
    res = 0
    while n > 0:
        res += n % x
        n = n // x
    return res


def main():
    N = NI()
    ans = 10**10
    for i in range(0, N+1, 6):
        ans = min(get_num_draw(N-i, 9) + get_num_draw(i//6, 6), ans)
    print(ans)


def __starting_point():
    main()
__starting_point()
