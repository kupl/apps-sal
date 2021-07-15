MOD = 10 ** 9 + 7
N = int(input())
C = list(map(int, input().split()))
C.sort()

if N == 1:
    print (2 * C[0] % MOD)
    return

ANS = 0
for i, c in enumerate(C):
    ANS += c * (N + 1 - i)

ANS *= pow(2, N - 2, MOD)
ANS %= MOD
ANS *= pow(2, N, MOD)
print (ANS % MOD)
