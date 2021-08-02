from collections import Counter
R = lambda: map(int, input().split())


def primefactors(n):
    f = 2
    while f * f <= n:
        while not n % f:
            yield f
            n //= f
        f += 1
    if n > 1:
        yield n


for _ in range(int(input())):
    n = int(input())
    dd = list(R())
    c = Counter()
    for d in dd:
        ct = Counter(primefactors(d))
        for k in ct: c[k] = max(c[k], ct[k])
    x = 1
    for k, v in c.items():
        x *= k**v
    if x == max(dd):
        t = min(dd)
        x *= t
        c[t] += 1
    m = 1
    for v in c.values(): m *= v + 1
    print(x if m == len(dd) + 2 else -1)
