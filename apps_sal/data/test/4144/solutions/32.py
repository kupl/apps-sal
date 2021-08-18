MOD = 10**9 + 7


def an(a, n):
    ans = 1
    for i in range(N):
        ans = ans * a % MOD
    return ans % MOD


N = int(input())


A_n0 = an(9, N)
A_n0n9 = an(8, N)


ans = 10**N % MOD - (2 * A_n0 % MOD - A_n0n9)
print(ans % MOD)
