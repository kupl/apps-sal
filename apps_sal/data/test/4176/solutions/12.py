import math
import collections
ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

a,b = mi()
print((a*b)//math.gcd(a,b))
