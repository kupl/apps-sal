mod = 998244353

def binpow(num, p):
    if(p == 0):
        return 1
    if(p % 2 == 0):
        return binpow((num * num) % mod, p // 2)
    return (num * binpow(num, p - 1)) % mod

def rev(num):
    return binpow(num, mod - 2)

def solve(a, b):
    result = 1
    prev = 1
    for k in range(1, min(a, b) + 1):
        now = (prev * (a - (k - 1)) * (b - (k - 1)) * rev(k)) % mod
        result  = (result + now) % mod
        prev = now
    return (result) % mod

a, b, c = list(map(int, input().split()))

res1 = solve(a, b)
res2 = solve(b, c)
res3 = solve(a, c)

print((res1 * res2 * res3) % mod)

