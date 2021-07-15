MOD = 10 ** 9 + 7

L = list(input())

N = len(L)

OK = [0] * (N + 1)
JUST = [0] * (N + 1)
JUST[0] = 1

for i in range(N):
    if L[i] == '1':
        OK[i + 1] = (OK[i] * 3 + JUST[i]) % MOD
        JUST[i + 1] = (JUST[i] * 2) % MOD
    else:
        OK[i + 1] = (OK[i] * 3) % MOD
        JUST[i + 1] = (JUST[i]) % MOD

print ((OK[-1] + JUST[-1]) % MOD)
