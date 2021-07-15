N = int(input())
C = list(map(int, input().split()))
C.sort(reverse =  True)

MOD = 10 ** 9 + 7

if N == 1:
    print (2 * C[0] % MOD)
    return

start = pow(2, N - 1, MOD)
step = pow(2, N - 2, MOD)
ans = 0
for c in C:
    ans += c * start
    ans %= MOD
    start += step
    start %= MOD

ans *= pow(2, N, MOD)
ans %= MOD

print (ans)
