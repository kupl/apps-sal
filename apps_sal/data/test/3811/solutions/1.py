def primes(n):
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            primfac.add(d)
            n //= d
        d += 1
    if n > 1:
        primfac.add(n)
    return primfac


n = int(input())
pairs = []
for i in range(n):
    pairs.append([int(i) for i in input().split()])
primfac = set()
primes(pairs[0][0])
primes(pairs[0][1])
for i in range(n - 1):
    to_delete = []
    for j in primfac:
        if pairs[i + 1][0] % j != 0 and pairs[i + 1][1] % j != 0:
            to_delete.append(j)
    for j in to_delete:
        primfac.remove(j)

li = list(primfac)
if len(li) == 0:
    print(-1)
else:
    print(li[-1])
