import fractions

n = int(input())
ns = list(map(int, input().strip().split(' ')))

a = []
skip = {}
ns = sorted(ns, reverse=True)

for i, num in enumerate(ns):
    if num in skip and skip[num] > 0:
        skip[num] -= 1
        continue

    a.append(num)
    if len(a) == n:
        break

    for other in a:
        gcd = fractions.gcd(other, num)
        if not gcd in skip:
            skip[gcd] = 0
        skip[gcd] += 2

print(' '.join(map(str, a)))
