X, Y = [int(_) for _ in input().split()]

p = 10 ** 9 + 7
N = 670000

fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((p - inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)
    
def combination(n, r, p):
    if r < 0 or n < r:
        return 0
    r = min(r, n-r)
    return fact[n] * factinv[r] * factinv[n-r] % p

def solve(X, Y):
    if (X + Y) % 3 != 0:
        return 0
    Z = (X + Y) // 3
    x = (Z + X - Y) // 2
    return combination(Z, x, p)

print((solve(X, Y)))

