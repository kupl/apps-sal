from math import log, ceil
n = int(input())

d = {}

def prime_fac(n):
    nonlocal d
    i = 2
    while i <= n:
        while n % i == 0 and i <= n:
            n //= i
            d[i] = d.get(i, 0) + 1
        i += 1
 
if n == 1:
    print(1, 0)
else:
    prime_fac(n)
    m = d[max(d, key=lambda x: d[x])]
    prod = 1
    for i in d:
        prod *= i
    if m in [2**i for i in range(50)] and len(set(d.values())) == 1:
        print(prod, int(log(m, 2)))
    else:
        print(prod, ceil(log(m, 2)) + 1)
