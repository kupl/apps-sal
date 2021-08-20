from collections import Counter
n = int(input())
f = Counter()
factors = []
for i in range(2, min(int(n ** 0.5 + 1), n + 1)):
    if n % i == 0:
        factors.append(i)
        factors.append(n // i)
factors.sort()
for factor in factors:
    while n % factor == 0:
        n //= factor
        f[factor] += 1


def bsearch(test, lo, hi):
    while lo != hi:
        mid = (lo + hi + 1) // 2
        if test(mid):
            lo = mid
        else:
            hi = mid - 1
    return lo


ans = 0
for (p, q) in list(f.items()):
    ans += bsearch(lambda w: w * (w + 1) // 2 <= q, 0, 10 ** 12)
if ans == 0 and n > 1:
    print(1)
else:
    print(ans)
