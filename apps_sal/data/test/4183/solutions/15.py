from math import gcd
n = int(input())
t = list([int(input()) for _ in range(n)])
x = 1
for i in t:
    x = x*i//gcd(x,i)
print(x)
