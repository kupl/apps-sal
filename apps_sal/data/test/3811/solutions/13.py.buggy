from math import gcd
n = int(input())
al = []
bl = []
g = 0
for _ in range(n):
    a, b = map(int, input().split())
    g = gcd(g, a * b)
    al.append(a)
    bl.append(b)
if(g == 1):
    print(-1)
    return
for i in range(n):
    x = gcd(g, al[i])
    if(x > 1):
        g = x
    x = gcd(g, bl[i])
    if(x > 1):
        g = x
if(g != 1):
    print(g)
else:
    print(-1)
