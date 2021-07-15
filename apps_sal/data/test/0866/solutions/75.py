X, Y = map(int, input().split())

def cmb(n, r, p):
    fact = [1, 1]
    factinv = [1, 1]
    inv = [0, 1] 

    for i in range(2, n+1):
        fact.append((fact[-1] * i) % p)
        inv.append((-inv[p % i] * (p // i)) % p)
        factinv.append((factinv[-1] * inv[-1]) % p)

    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

s = X+Y

if s%3 != 0:
    print(0)
else:
    a = (s//3-(X-Y))//2
    print(cmb(s//3, a, 10**9+7))
