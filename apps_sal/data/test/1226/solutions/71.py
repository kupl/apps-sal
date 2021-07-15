n, a, b = map(int, input().split())

MOD = 10**9 + 7
N = pow(2,n,MOD)

def com(n,r):
    s = 1
    for i in range(n-r+1, n+1):
        s *= i
        s %= MOD

    t = 1
    for j in range(1,r+1):
        t *= j
        t %= MOD


    return s * pow(t,MOD-2, MOD) % MOD

print((N - com(n, a) - com(n, b) - 1) % (MOD))
