n, a, b = list(map(int, input().split()))
if a > b: a, b = b, a
mod = 10 ** 9 + 7
tmp = 1

C = n
ans = 0
if a == 1: Ca = n
for r in range(1, n + 1):
    C = (((C * (n - r)) % mod )* pow(r + 1, mod - 2, mod)) % mod
    if r == a - 1:
        Ca = C
    if r == b - 1:
        Cb = C
        break

print(((pow(2, n, mod) - Ca - Cb - 1) % mod))

