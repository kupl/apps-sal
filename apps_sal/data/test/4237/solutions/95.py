import math
def lcm(x, y):
    return (x * y) // math.gcd(x, y)
A, B, C, D = map(int,input().split())
Cres = B//C - (A-1)//C
Dres = B//D - (A-1)//D
CDres = B//lcm(C,D) - (A-1)//lcm(C,D)
print(B-A+1-(Cres + Dres - CDres))
