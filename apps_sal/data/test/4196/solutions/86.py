from math import gcd
n = int(input())
a = list(map(int, input().split()))
l = [a[-1], a[0]]
r = [a[-1]]
for x in a[1:-1]:
    l.append(gcd(l[-1], x))
for x in a[-2:0:-1]:
    r.append(gcd(r[-1], x))
r = r[::-1]
r.append(a[0])
print(max((gcd(l[i], r[i]) for i in range(n))))
