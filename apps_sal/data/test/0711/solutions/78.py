
def resolve():
    # nCk = n! / n!(n-k)! のテーブル作成
    def COMinit(n, MOD):
        fact = [1, 1]
        fact_inv = [1, 1]
        inv = [0, 1]
        for i in range(2, n + 1):
            fact.append((fact[-1] * i) % MOD)
            inv.append((-inv[MOD % i] * (MOD // i)) % MOD)
            fact_inv.append((fact_inv[-1] * inv[i]) % MOD)
        return fact, fact_inv

    # 二項係数計算
    def Combination(n, k, MOD=10 ** 9 + 7):
        fac, finv = COMinit(n, MOD)
        if n < k:
            return 0
        if n < 0 or k < 0:
            return 0
        ret = fac[n] * finv[k] * finv[n - k] % MOD
        return ret

    # 指数:exponent
    def dic_factorization(n):
        arr = []
        temp = n
        for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
            if temp % i == 0:
                cnt = 0
                while temp % i == 0:
                    cnt += 1
                    temp //= i
                arr.append([i, cnt])
        if temp != 1:
            arr.append([temp, 1])
        if arr == []:
            arr.append([n, 1])
        return arr

    MOD = 10**9 + 7
    N, M = map(int, input().split())
    if M == 1:
        print(1)
        return

    fact = dic_factorization(M)
    ans = 1
    for v in fact:
        ans *= Combination(N + v[1] - 1, v[1])
        ans %= MOD

    print(ans)


def __starting_point():
    resolve()


__starting_point()
