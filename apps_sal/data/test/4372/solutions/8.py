from math import gcd
n = int(input())
a = sorted(list(map(int,input().split())))
s = sum(a)-a[n-1]
t = a[n-1]*(n-1)
ans = t-s
g = a[n-1]-a[0]
for i in range(1,n-1):
    g = gcd(a[n-1]-a[i],g)
print(ans//g,g)

