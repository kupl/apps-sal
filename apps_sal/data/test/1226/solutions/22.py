import sys

N_MAX = 200000 + 5
INF = 10**9 + 7
sys.setrecursionlimit(N_MAX)
MOD = 10**9 + 7

# ## COMBINATION (MOD) ## #
MOD = 10**9 + 7  # , N = 2*10**5 で 0.3s
N_MAX = 2 * 10**5  # 問題サイズに合わせて変えておく

fac = [1, 1]  # 元テーブル
facinv = [1, 1]  # 逆元テーブル
inv = [0, 1]  # 逆元テーブル計算用テーブル

for i in range(2, N_MAX + 1):
    fac.append((fac[-1] * i) % MOD)
    inv.append((-inv[MOD % i] * (MOD // i)) % MOD)
    facinv.append((facinv[-1] * inv[-1]) % MOD)


def fac(n, a):
    ans = 1
    for i in range(a):
        ans *= n
        ans %= MOD
        n -= 1
    return ans


def cmb(n, r):
    if (r < 0 or r > n):
        return 0
    # r = min(r, n-r)
    return fac[n] * facinv[r] * facinv[n - r] % MOD


def main():
    n, a, b = map(int, sys.stdin.readline().rstrip().split())

    # 全種類
    ans = pow(2, n, MOD) - 1  # -1 : 全部選ばない場合
    ans %= MOD

    # a種類になる場合
    ans -= fac(n, a) * facinv[a]
    ans %= MOD

    ans -= fac(n, b) * facinv[b]
    ans %= MOD

    print(ans)


main()
