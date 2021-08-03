from math import gcd
n, x = list(map(int, input().split()))
ls = sorted(list(map(int, input().split())))
if x == 1:
    print((abs(x - ls[0])))
    return
distant = []
for i in range(n):
    diff = abs(ls[i] - x)
    distant.append(diff)
distant.sort()
a = distant[0]
for i in distant:
    g = gcd(a, i)
    a = g
print(g)
