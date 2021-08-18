N, M, K = list(map(int, input().split()))
mod = 10**9 + 7


factorial = [1 for i in range(N * M + 1)]
for i in range(1, N * M + 1):
    if i == 1:
        factorial[i] = 1
    else:
        factorial[i] = factorial[i - 1] * i % mod


def comb(n, k):
    return (factorial[n] * pow(factorial[n - k] * factorial[k], -1, mod)) % mod


xscore = 0
for i in range(1, N):
    xscore += i * (N - i)
xscore %= mod
xscore *= M**2 * comb(N * M - 2, K - 2)
xscore %= mod

yscore = 0
for i in range(1, M):
    yscore += i * (M - i)
yscore %= mod
yscore *= N**2 * comb(N * M - 2, K - 2)
yscore %= mod

print(((xscore + yscore) % mod))
