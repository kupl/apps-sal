from math import gcd
def lcm(x,y):
    return x*y//gcd(x,y)
def cnt(x):
    i = 0
    while x%2 == 0:
        x = x//2
        i += 1
    return i 
n,m = map(int,input().split())
a = list(map(int,input().split()))
memo = cnt(a[0])
for i in range(n):
    if cnt(a[i]) != memo:
        print(0)
        return
    a[i] = a[i]//2

t = 1
for i in range(n):
    t = lcm(t,a[i])
print(m//t-m//(2*t))
