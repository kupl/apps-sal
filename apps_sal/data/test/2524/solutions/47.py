import numpy as np
INT = lambda: int(input())
INTM = lambda: map(int, input().split())
STRM = lambda: map(str, input().split())
STR = lambda: str(input())
LIST = lambda: list(map(int, input().split()))
LISTS = lambda: list(map(str, input().split()))


def do():
    n = INT()
    a = np.array(LIST())
    ans = 0
    mod = 10**9 + 7
    for i in range(70):
        digit = np.sum((a >> i) & 1)
        ans += pow(2, i, mod) * (((n - digit) * digit) % mod) % mod
        ans = ans % mod

    print(ans)


def __starting_point():
    do()


__starting_point()
