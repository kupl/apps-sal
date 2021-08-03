import sys


# ## COMBINATION (MOD) ## #
MOD = 10**9 + 7  # , N = 2*10**5 で 0.3s
N_MAX = 10**5 + 1  # 問題サイズに合わせて変えておく

fac = [1, 1]  # 元テーブル
facinv = [1, 1]  # 逆元テーブル
inv = [0, 1]  # 逆元テーブル計算用テーブル

for i in range(2, N_MAX + 1):
    fac.append((fac[-1] * i) % MOD)
    inv.append((-inv[MOD % i] * (MOD // i)) % MOD)
    facinv.append((facinv[-1] * inv[-1]) % MOD)


def cmb(n, r):
    if (r < 0 or r > n):
        return 0
    # r = min(r, n-r)
    return fac[n] * facinv[r] * facinv[n - r] % MOD


def main():
    N, K = list(map(int, sys.stdin.readline().rstrip().split()))
    A = [int(x) for x in sys.stdin.readline().rstrip().split()]

    A.sort()  # 小 -> 大

    # 左から i 番目が選ばれて、i+1番目以降が選ばれない
    sum = 0
    for i in range(N - K + 1):
        sum += cmb(N - i - 1, K - 1) * (A[-(i + 1)] - A[i]) % MOD
        sum %= MOD

    print(sum)


main()
