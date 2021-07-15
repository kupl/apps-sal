import math        # factorical（階乗) # hypot(距離)
# import heapq
# from fractions import gcd # Python3.5以前 # lcm（最小公倍数） = (a*b)//gcd(a,b)
# from fractions import Fraction
# from math import gcd # Python3.6以降
# --------------------------------------------------------------

a,b,x = list(map(int,input().split()))

if x*2 <= a*a*b:
    print((math.degrees(math.atan(a*b*b/(2*x)))))
else:
    print((math.degrees(math.atan((a*a*b-x)*2/(a**3)))))

