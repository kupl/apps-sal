import math
def lcm(x, y):
    return (x * y) // math.gcd(x, y)

N=int(input())
a=int(input())
for i in range(N-1):
    a=lcm(a,int(input()))
print(a)

