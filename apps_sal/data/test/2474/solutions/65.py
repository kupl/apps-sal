MOD = 10**9 + 7
N = int(input())
clist = list(map(int, input().split()))
clist.sort()


def powmod(a, p):
    if p == 0:
        return 1
    elif p == 1:
        return a
    else:
        pow2 = powmod(a, p // 2)
        if p % 2 == 0:
            return (pow2**2) % MOD
        else:
            return (a * pow2**2) % MOD


base = powmod(2, 2 * N - 2)
coef = 0
for i in range(N):
    coef += clist[i] * (N + 1 - i)
    coef %= MOD

print(base * coef % MOD)
