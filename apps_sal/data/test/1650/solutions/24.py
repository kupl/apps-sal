import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    L = input()
    n = len(L)

    res = 0
    cnt = 0
    for i in range(n):
        if L[i] == "1":
            rest = n - (i + 1)
            res += pow(2, cnt, mod) * pow(3, rest, mod) % mod
            res %= mod
            cnt += 1

    res += pow(2, cnt, mod)
    print((res % mod))


def resolve2():
    """
    桁DP
    """
    L = input().rstrip()
    n = len(L)

    # dp[i][0]:Lを上からi桁目まで見た時、Lと一致するような組み合わせ
    # dp[i][1]:Lを上からi桁目まで見た時、L未満になるような組み合わせ
    dp = [[0] * 2 for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        if L[i - 1] == "0":
            # 今見ている桁が0でありそれ以前の数値がLと一致していれば、i桁目まで一致する条件にあてはまる組み合わせは(0,0)のみ
            dp[i][0] = dp[i - 1][0]
            # 今見ている桁が0でありそれ以前の数値がL未満であれば、どの組み合わせでもL未満になる(0,0)(0,1)(1,0)
            dp[i][1] = (dp[i - 1][1] * 3) % mod
        else:
            # 今見ている桁が1でありそれ以前の数値がLと一致していれば、i桁目まで一致する条件にあてはまる組み合わせは(0,1),(1,0)のみ
            dp[i][0] = (dp[i - 1][0] * 2) % mod
            # 今見ている桁が1でありそれ以前の数値がL未満であれば、どの組み合わせでもL未満になる(0,0)(0,1)(1,0)
            # 今見ている桁が1でありそれ以前の数値が一致していれば、L未満になる組み合わせは(0,0)のみ
            dp[i][1] = (dp[i - 1][1] * 3 + dp[i - 1][0]) % mod

    print(((dp[n][0] + dp[n][1]) % mod))


def __starting_point():
    resolve2()


__starting_point()
