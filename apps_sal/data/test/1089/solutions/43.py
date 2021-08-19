N, M, K = list(map(int, input().split()))
mod = 10**9 + 7

# N行, M列 i-j
# 1-1, 1-2, 1-3, 1-4, ... , 1-M
# 2-1, 2-2, 2-3, 2-4, ... , 2-M
# 3-1. 3-2. 3-3, 3-4, ... , 3-M
# ...
# N-1, N-2, N-3, N-4, ... , N-M

# K個の駒が上記の座表上に置かれた時の配置全種類のコストの総和を調べたい

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
