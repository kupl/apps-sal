import functools

@functools.lru_cache(maxsize=10000)
def factor(n):
    res = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            res.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        res.append(n)
    return set(res)

num = int(input())

poks = list(map(int, input().split()))[:num]

c = dict()
for p in poks:
    for d in factor(p):
        if d in c.keys():
            c[d] += 1
        else:
            c[d] = 1
            
if c:
    print(max(c.values()))
else:
    print(1)
