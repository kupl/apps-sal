import math
n = int(input())
a = list(map(int, input().split()))
l = max(a)
c = []
for i in range(len(a)):
    c.append(l - a[i])
p = 0
for i in range(len(c)):
    p = math.gcd(p, c[i])
o = sum(c)
print(o // p, p)
