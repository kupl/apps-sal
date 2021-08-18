def f_coincidence(MOD=10 ** 9 + 7):
    from itertools import product
    L, R = [int(i) for i in input().split()]

    dp = [[[[0 for s in range(2)] for k in range(2)]
           for j in range(2)] for i in range(61)]
    dp[60][0][0][0] = 1

    for i in range(59, -1, -1):
        lb = (L >> i) & 1
        rb = (R >> i) & 1

        r2 = range(2)
        for j, k, s in product(r2, r2, r2):
            pre = dp[i + 1][j][k][s]
            for xb, yb in product(r2, r2):
                if xb == 1 and yb == 0:
                    continue

                nj, nk, ns = j, k, s
                if s == 0 and xb != yb:
                    continue
                if s == 0 and xb == 1 and yb == 1:
                    ns = 1

                if j == 0 and xb == 0 and lb == 1:
                    continue
                if j == 0 and xb == 1 and lb == 0:
                    nj = 1

                if k == 0 and yb == 1 and rb == 0:
                    continue
                if k == 0 and yb == 0 and rb == 1:
                    nk = 1

                dp[i][nj][nk][ns] += pre
                dp[i][nj][nk][ns] %= MOD

    ans = sum([dp[0][j][k][s] for j in range(2) for k in range(2)
               for s in range(2)]) % MOD
    return ans


print(f_coincidence())
