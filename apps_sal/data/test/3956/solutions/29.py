mod = 998244353
(K, N) = list(map(int, input().split()))
Factorial = [1] * (N + K + 1)
for i in range(1, N + K + 1):
    Factorial[i] = Factorial[i - 1] * i % mod


def power(x, y):
    if y == 0:
        return 1
    elif y == 1:
        return x % mod
    elif y % 2 == 0:
        return power(x, y // 2) ** 2 % mod
    else:
        return power(x, y // 2) ** 2 * x % mod


inverseFactorial = [1] * (N + K + 1)
inverseFactorial[N + K] = power(Factorial[N + K], mod - 2)
for i in range(0, N + K)[::-1]:
    inverseFactorial[i] = inverseFactorial[i + 1] * (i + 1) % mod


def C(x, y):
    if x < y or y < 0:
        return 0
    else:
        return Factorial[x] * inverseFactorial[y] * inverseFactorial[x - y] % mod


def H(x, y):
    return C(x + y - 1, y)


def ans(M, N, K):
    res = 0
    for m in range(1, M + 1)[::-1]:
        if m % 2:
            res += C(M, m) * H(K, N - 2 * m)
        else:
            res += -1 * C(M, m) * H(K, N - 2 * m)
    return (H(K, N) - res) % mod


for i in range(2, 2 * K + 1):
    if i % 2:
        print(ans(min(K, i - 1) - i // 2, N, K))
    else:
        print((ans(min(K, i - 1) - i // 2, N - 1, K - 1) + ans(min(K, i - 1) - i // 2, N, K - 1)) % mod)
