def primefactor(p):
    x = p
    pf = []
    for i in range(2, int(p**0.5) + 1):
        if(x % i == 0):
            pf.append(i)
            while(x % i == 0):
                x //= i
    if x > 1:
        pf.append(x)
    return pf


ans = 1
MOD = int(1e9 + 7)
x, n = list(map(int, input().split()))
for p in primefactor(x):
    exp = 0
    P = p
    while(P <= n):
        exp += n // P
        P *= p
    ans *= pow(p, exp, MOD)
    ans %= MOD
print(ans)
