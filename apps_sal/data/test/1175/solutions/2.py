def f_coincidence(MOD=10 ** 9 + 7):
    # 参考: https://atcoder.jp/contests/abc138/submissions/7013926
    from itertools import product
    L, R = [int(i) for i in input().split()]

    dp = [[[[0 for s in range(2)] for k in range(2)]
           for j in range(2)] for i in range(61)]
    dp[60][0][0][0] = 1

    for i in range(59, -1, -1):
        lb = (L >> i) & 1  # 'b' はビット値であることを示す(以下も同じ)
        rb = (R >> i) & 1

        r2 = range(2)
        for j, k, s in product(r2, r2, r2):
            pre = dp[i + 1][j][k][s]
            # ビットごとに値を試す
            for xb, yb in product(r2, r2):
                # editorial の通り、このビットの組は元の条件を満たさない
                if xb == 1 and yb == 0:
                    continue
                # editorial の通り、これ以降は x <= y が満たされる

                nj, nk, ns = j, k, s
                # 今注目している桁でMSBが立つか？
                if s == 0 and xb != yb:
                    continue  # どちらかが立っていない
                if s == 0 and xb == 1 and yb == 1:
                    ns = 1  # ここで初めてMSBが立った

                # L <= x を満たすか？
                if j == 0 and xb == 0 and lb == 1:
                    # jが0のまま xb<lb となれば、L<=xになりようがない
                    # jが1なら、xbとlbがどうなっていようがL<=xである
                    continue
                if j == 0 and xb == 1 and lb == 0:
                    nj = 1  # この桁で L<=x が確定する

                # y <= R を満たすか？
                if k == 0 and yb == 1 and rb == 0:
                    continue  # L<=x の場合分けと同じこと
                if k == 0 and yb == 0 and rb == 1:
                    nk = 1

                # 反映
                dp[i][nj][nk][ns] += pre
                dp[i][nj][nk][ns] %= MOD

    ans = sum([dp[0][j][k][s] for j in range(2) for k in range(2)
               for s in range(2)]) % MOD
    return ans


print(f_coincidence())
