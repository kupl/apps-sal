from math import gcd
n = int(input())
k = []
p = []
arr = [int(x) for x in input().split()]
g = max(arr)
print(g, end=' ')
for i in arr:
    if g % i == 0 and i not in k:
        k.append(i)
    else:
        p.append(i)
lcm = p[0]
for i in p[1:]:
    lcm = lcm * i // gcd(lcm, i)
print(lcm)
