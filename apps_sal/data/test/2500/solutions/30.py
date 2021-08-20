def d_XorSum(N):
    MOD = 10 ** 9 + 7
    memo = {0: 1, 1: 2}

    def f(k):
        if k in memo:
            return memo[k]
        ret = (f(k // 2) + f((k - 1) // 2) + f((k - 2) // 2)) % MOD
        memo[k] = ret
        return ret
    return f(N)


N = int(input())
print(d_XorSum(N))
