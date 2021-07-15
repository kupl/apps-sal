from math import gcd
def lcm(a,b):
    return a*b // gcd(a,b)
n = int(input())
a = 2
for i in range(3,n+1):
    a = lcm(a,i)
print(a+1)
