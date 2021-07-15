from math import gcd
n = int(input())
a = list(map(int,input().split()))
l = 0
r = 0
x = [0] * (n+1)
y = [0] * (n+1)
for i in range(n):
    x[i+1] = gcd(x[i],a[i])
for i in range(n)[::-1]:
    y[i] = gcd(y[i+1],a[i])
m = []
for i in range(n):
    m.append(gcd(x[i],y[i+1]))
print(max(m))
