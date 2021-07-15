MOD = 10**9 + 7
x, n = [int(item) for item in input().split()]
def prime_factorize(n):
    b = 2
    fct = set() 
    while b * b <= n:
        while n % b == 0:
            n //= b
            fct.add(b)
        b = b + 1
    if n > 1:
        fct.add(n)
    return fct

fac = prime_factorize(x)
ans = 1
for f in fac:
    cnt = 0
    val = n
    while val:
        cnt += val // f
        val //= f
    ans *= pow(f, cnt, MOD)
    ans %= MOD

print(ans)
