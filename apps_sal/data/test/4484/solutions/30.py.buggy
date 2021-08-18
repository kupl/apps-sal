N, M = map(int, input().split())
mod = 10**9 + 7

factorial = [1 for i in range(10**5 + 5)]
for i in range(1, 10**5 + 5):
    if i == 1:
        factorial[i] = 1
    else:
        factorial[i] = factorial[i - 1] * i % mod

if abs(N - M) > 1:
    print(0)
    return

if N == M:
    print(factorial[M]**2 * 2 % mod)
else:
    print(factorial[M] * factorial[N] % mod)
