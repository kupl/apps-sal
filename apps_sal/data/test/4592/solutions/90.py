n = int(input())
# a,b=map(int,input().split())
# l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]


def prime_factorize(n):
    n_origin = n + 0
    primelist = []
    a = 2
    while a * a <= n_origin:
        if n % a != 0:
            a += 1
            continue
        ex = 0
        while n % a == 0:
            ex += 1
            n = n // a
        primelist.append([a, ex])
        a += 1
    if n != 1:
        primelist.append([n, 1])
    return primelist


ex = {}
mod = 10**9 + 7
for i in range(2, n + 1):
    res = prime_factorize(i)
    for p, e in res:
        ex[p] = ex.get(p, 0) + e

ans = 1
for k, v in ex.items():
    ans = (ans * (v + 1)) % mod
print(ans)
