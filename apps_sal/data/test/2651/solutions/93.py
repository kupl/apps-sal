import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = list(map(int, input().split()))
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))

    XL = [X[i] - X[i - 1] for i in range(1, n)]
    YL = [Y[i] - Y[i - 1] for i in range(1, m)]

    cnt_X = [(i * (n - i)) % mod for i in range(1, n)]
    cnt_Y = [(i * (m - i)) % mod for i in range(1, m)]
    total_X = (sum([(XL[i] * cnt_X[i]) % mod for i in range(n - 1)])) % mod
    total_Y = (sum([(YL[i] * cnt_Y[i]) % mod for i in range(m - 1)])) % mod
    res = (total_X * total_Y) % mod
    print(res)


def __starting_point():
    resolve()


__starting_point()
