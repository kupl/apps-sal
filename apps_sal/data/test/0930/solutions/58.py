
DIV = 10 ** 9 + 7
n = 10**6
g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]

for i in range(2, n + 1):
    g1.append((g1[-1] * i) % DIV)
    inverse.append((-inverse[DIV % i] * (DIV // i)) % DIV)
    g2.append((g2[-1] * inverse[-1]) % DIV)


def nCr(n, r, DIV):
    if (r < 0 or r > n):
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % DIV


N, K = map(int, input().split())


ans = 0
for i in range(min(K, N - 1) + 1):
    a = nCr(N, i, DIV)

    b = nCr(N - 1, i, DIV)

    ans += (a * b) % DIV
    ans %= DIV

print(ans)
