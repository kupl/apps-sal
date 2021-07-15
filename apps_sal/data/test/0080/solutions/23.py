n = input()
arr = n.split(' ')
arr = list(map(lambda x: int(x), arr))
l,r,x,y = arr
gcd = x
lcm = y
from math import sqrt
from fractions import gcd
def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return int(a * b / gcd(a, b))

ab = x * y
ans = 0
# for a in range(l, r+1):
#     if(a > sqrt(r+1) + 100000):
#         break
#     if(ab % a == 0):
#         b = ab / a
#         if(a > b):
#             break
#         if(l <= b and b <= r and lcm(a,b) == y):
#             if(ab / a == a):
#                 ans += 1
#             else: 
#                 ans += 2
a = x
# while(a % x != 0):
#     a += 1
while(a <= sqrt(ab)):
    b = int(ab / a)
    if(a > b):
        break
    if(ab % a == 0):
        if(l <= b and b <= r and lcm(a,b) == y and l <= a and a <= r):
            if(b == a):
                ans += 1
            else: 
                ans += 2
    a += x

print(ans)
