import itertools   # accumulate, compress, permutations(nPr), combinations(nCr)
import bisect      # bisect_left(insert位置), bisect_right(slice用)
# import math        # factorical（階乗) # hypot(距離)
# import heapq
# from fractions import gcd # Python3.5以前 # lcm（最小公倍数） = (a*b)//gcd(a,b)
# from fractions import Fraction
# from math import gcd # Python3.6以降
# --------------------------------------------------------------

n  = int(input())
bo = list(map(int,input().split()))
 
cnt = 0
bo.sort()
 
for a in range(n-1):
    for b in range(a+1,n):
        cnt += bisect.bisect_left(bo, bo[a]+bo[b]) - (b+1)

print(cnt)
