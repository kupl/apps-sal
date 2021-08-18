n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort(reverse=True)
mod = 10**9 + 7


def cmb(n, r, mod):
    if (r < 0 or r > n):
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod


g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]

for i in range(2, 10**5 + 5):
    g1.append((g1[-1] * i) % mod)
    inverse.append((-inverse[mod % i] * (mod // i)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)


ans = 0
for i in range(0, n - k + 1):
    ans += a[i] * cmb(n - i - 1, k - 1, mod)
    ans %= mod

a.sort()
for i in range(0, n - k + 1):
    ans -= a[i] * cmb(n - i - 1, k - 1, mod)
    ans %= mod

print(ans)
