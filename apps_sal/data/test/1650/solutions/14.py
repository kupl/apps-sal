L = input()

N = len(L)
mod = int(1e9 + 7)

dp1 = [0] * N
dp2 = [0] * N

dp1[0] = 1
dp2[0] = 2

for i in range(1, N):
    dp1[i] += dp1[i - 1] * 3
    dp1[i] %= mod
    if L[i] == '1':
        dp1[i] += dp2[i - 1]
        dp2[i] += dp2[i - 1] * 2
    else:
        dp2[i] += dp2[i - 1]
    dp1[i] %= mod
    dp2[i] %= mod

print((dp1[N - 1] + dp2[N - 1]) % mod)
