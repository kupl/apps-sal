from math import sqrt
from sys import stdin
a = set()
n = int(stdin.readline())
n2 = sqrt(n)
t = 2
while t <= n2 and n > 1:
    if n % t == 0:
        n //= t
        a.add(t)
        t = 1
        n2 = sqrt(n)
    t += 1
a.add(n)
q = 1
for x in a:
    q *= x
print(q)
