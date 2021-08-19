(H, W, A, B) = list(map(int, input().split()))
mod = 10 ** 9 + 7
U = 2 * 10 ** 5
factorial = [1 for _ in range(U + 1)]
for i in range(1, U + 1):
    factorial[i] = factorial[i - 1] * i % mod
inverse = [1 for _ in range(U + 1)]
inverse[U] = pow(factorial[U], mod - 2, mod)
for i in range(U, 0, -1):
    inverse[i - 1] = inverse[i] * i % mod


def comb(n, k):
    if k < 0 or k > n:
        return 0
    x = factorial[n]
    x *= inverse[k]
    x %= mod
    x *= inverse[n - k]
    x %= mod
    return x


ans = 0
for i in range(H - A):
    x = comb(B - 1 + i, i)
    a = H - 1 - i
    b = W - 1 - B
    x *= comb(a + b, a)
    x %= mod
    ans += x
ans %= mod
print(ans)
