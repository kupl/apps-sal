from math import log2
pricey = 9 ** 99
x = set()
match = ['A', 'B', 'C', 'AB', 'BC', 'AC', 'ABC']
n = int(input())
cheapest = [100001] * 7
for i in range(n):
    (p, s) = input().split()
    p = int(p)
    for c in s:
        x.add(c)
    s = ''.join(sorted(list(s)))
    j = match.index(s)
    cheapest[j] = min(cheapest[j], p)
if len(x) < 3:
    print(-1)
else:
    for i in range(1, 128):
        truth = [int(i) for i in '0' * (6 - int(log2(i))) + bin(i)[2:]]
        price = 0
        has = set()
        for (j, b) in enumerate(truth):
            if b:
                if cheapest[j] > 100000:
                    break
                else:
                    price += cheapest[j]
                    for c in match[j]:
                        has.add(c)
        else:
            if len(has) == 3:
                pricey = min(price, pricey)
    print(pricey)
