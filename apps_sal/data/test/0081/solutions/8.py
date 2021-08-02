from math import gcd

a, b = list(map(int, input().split()))
f = abs(a - b)
d = []
i = 1
while i * i <= f:
    if f % i == 0:
        d.append(i)
        d.append(f // i)
    i += 1

d = list(set(d))
d.sort()


def f(i):
    return (a + i) * (b + i) // gcd(a + i, b + i)


x = float('inf')
y = 0
for i in d:
    k = (i - a % i) % i
    z = f(k)
    if z < x:
        x = z
        y = k

print(y)
