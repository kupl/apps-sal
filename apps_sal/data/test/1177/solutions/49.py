def main():
    import sys
    sys.setrecursionlimit(10**9)
    input = sys.stdin.readline
    import numpy as np

    mod = 998244353

    N, S = map(int, input().split())
    A = list(map(int, input().split()))

    # 多項式
    polynomial = np.zeros(S + 1, int)
    ans = 0
    for i in A:
        polynomial[0] += 1
        polynomial[i:] += polynomial[:-i].copy()
        polynomial %= mod
        ans += polynomial[S]

    print(ans % mod)


main()
