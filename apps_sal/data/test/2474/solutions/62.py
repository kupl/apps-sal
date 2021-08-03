N = int(input())
mod = int(1e9) + 7
C = list(map(int, input().split()))
C.sort(reverse=True)


def doubling(n, m):
    y = 1
    base = n
    while m != 0:
        if m % 2 == 1:
            y *= base
            y %= mod
        base *= base
        base %= mod
        m //= 2
    return y


b = 1
if N == 1:
    L, R = 0, 1
else:
    b = doubling(2, N - 2)
    L, R = b, (2 * b) % mod
S1 = 0
S2 = 0
for i in range(N):
    S1 += (i * C[i]) % mod
    S1 %= mod
    S2 += C[i]
    S2 %= mod
print((doubling(2, N) * (S1 * L + S2 * R)) % mod)
