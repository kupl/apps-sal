def nCr(n, r, mod):
    if (r < 0 or r > n):
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod


mod = 10**9 + 7
size = 10**6
g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]

for i in range(2, size + 1):
    g1.append((g1[-1] * i) % mod)
    inverse.append((-inverse[mod % i] * (mod // i)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append(cnt)

    if temp != 1:
        arr.append(1)

    return arr


N, M = map(int, input().split())
L = factorization(M)

ans = 1

for i in L:
    ans *= nCr(i + N - 1, N - 1, mod)
    ans %= mod

print(ans)
