r1, c1, r2, c2 = map(int, input().split())

n = [1] * (r2 + c2 + 3)
mod = 10**9 + 7
for i in range(r2 + c2 + 2):
    n[i + 1] = (n[i] * ((i + 1) % mod)) % mod


def calc(r, c):
    x = n[r + c] % mod
    y = (n[r] * n[c]) % mod
    return (x * (pow(y, mod - 2, mod) % mod)) % mod


ans = calc(r2 + 1, c2 + 1) - calc(r2 + 1, c1) - calc(r1, c2 + 1) + calc(r1, c1)
ans %= mod

print(ans)
