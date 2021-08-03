import numpy as np


def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = np.array(a, dtype='int64')
    mod = 10**9 + 7
    div, ans = 1, 0
    for i in range(60):
        ca = (a >> i) & 1
        cnt = int(ca.sum())
        ans += (cnt * (n - cnt) * div) % mod
        div = (div * 2) % mod
    print(ans % mod)


def __starting_point():
    main()


__starting_point()
