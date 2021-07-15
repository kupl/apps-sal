import math
N = int(input())
def lcm(a,b):
    return int(a*b//math.gcd(a,b))
print(lcm(2,N))
