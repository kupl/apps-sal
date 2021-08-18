def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


n = int(input())
np = set(prime_factorize(n))
npl = []
for i in np:
    j = 1
    j *= i
    while j <= n:
        npl.append(j)
        j *= i
npl.sort()

cz = 2
ans = 0
for cz in npl:
    if cz > n:
        break
    if n % cz == 0:
        ans += 1
        n //= cz
print(ans)
