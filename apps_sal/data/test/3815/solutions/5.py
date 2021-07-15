n, a, b, k = map(int, input().split())
s = input()
mod = int(1e9 + 9)
inv = lambda x: pow(x, mod-2, mod)
q = pow(b, k, mod) * inv(pow(a, k, mod)) % mod
per = 0
d = pow(a, n, mod)
qq = b * inv(a) % mod
for i in range(k):
    if s[i] == '+':
        per += d
    else:
        per -= d
    per %= mod
    d = d * qq % mod
t = (n + 1) // k
if q == 1:
    print(t * per % mod)
    return
z = (pow(q, t, mod) - 1) * inv(q-1) % mod
print(z * per % mod)
