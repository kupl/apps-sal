from math import gcd
N = int(input())
def lcm(a,b):
    return a*b//gcd(a,b)

T1 = int(input())
ans = T1
for i in range(N-1):
    T2 = int(input())
    ans = lcm(ans,T2)
    T1 = T2

print(ans)
