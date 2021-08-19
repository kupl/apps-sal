n, m = map(int, input().split())
mod = 10**9 + 7
nums = 5 * (10**5)  # 制約に合わせよう

g1, g2, inverse = [1, 1], [1, 1], [0, 1]

for num in range(2, nums + 1):
    g1.append((g1[-1] * num) % mod)
    inverse.append((-inverse[mod % num] * (mod // num)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)


def nPr(n, r):
    return g1[n] * g2[n - r] % mod


def nCr(n, r):
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod


ans = 0
for r in range(n + 1):
    tmp = nCr(n, r) * nPr(m, r) * (nPr(m - r, n - r)**2) % mod
    ans = (ans + (-1)**r * tmp) % mod
print(ans)
