from fractions import gcd

n = int(input())
a = input().split()
a = [int(i) for i in a]

g = a[0]

for i in a:
    g = gcd(i, g)

if g in a:
    print(g)
else:
    print(-1)
