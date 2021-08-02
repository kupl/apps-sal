n, a, b = map(int, input().split())

mod = 10**9 + 7

ans = pow(2, n, mod)

ans -= 1

aa = 1
for i in range(1, a + 1):
    aa = (aa * (n - i + 1) * pow(i, -1, mod)) % mod

bb = 1
for i in range(1, b + 1):
    bb = (bb * (n - i + 1) * pow(i, -1, mod)) % mod

ans = (ans - aa - bb) % mod

print(ans)
