def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

p = 10 ** 9 + 7
N = 10 ** 6
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]
 
for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

x, y = map(int,input().split())

if (x+y)%3:
    ans = 0
else:
    n = (x+y)//3
    x -= n
    y -= n
    if (x<0) or (y<0):
        ans = 0
    else:
        ans = cmb(x+y,y,p)

print(ans)
