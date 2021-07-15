# 解説放送

def pow2(n, mod):
    """2のn乗まで"""
    t = 1
    yield t
    for _ in range(n):
        t = t * 2 % mod
        yield t


def main():
    MOD = 10 ** 9 + 7

    N = int(input())
    *c, = list(map(int, input().split()))

    c.sort()

    *two, = pow2(N, MOD)

    ans = 0
    for l, x in enumerate(c):
        # x:=係数.この位置の操作にかかるコストの総和を求める.
        # r:=xの右側にある要素数
        # (1<<r)個の状態を行として並べて,列で不一致数を確認すると,どの列も状態の半分が不一致.これがr列ある.
        r = N - l - 1

        t = two[r]
        if r != 0:
            t += two[r - 1] * r  # 右側の個数
        t = t * two[l] % MOD
        t = t * x % MOD
        ans += t

    ans = ans * two[N] % MOD
    print(ans)


def __starting_point():
    main()

__starting_point()
