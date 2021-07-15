from itertools import product

def factorize(n):
    res = []
    if n % 2 == 0:
        power = 0
        while n % 2 == 0:
            power += 1
            n //= 2
        res.append((2, power))
    i = 3
    while i * i <= n:
        if n % i == 0:
            power = 0
            while n % i == 0:
                power += 1
                n //= i
            res.append((i, power))
        i += 2
    if n > 1:
        res.append((n, 1))
    return res

l, r, x, y = [int(x) for x in input().split()]

if y % x:
    print(0)
    return

diff = y // x

facs = [p ** power for p, power in factorize(diff)]

res = 0
for i in range(2 ** len(facs)):
    fac1 = x
    for j in range(len(facs)):
        if (1 << j) & i: fac1 *= facs[j]
    fac2 = x * y // fac1
    if l <= fac1 <= r and l <= fac2 <= r:
        res += 1
print(res)
