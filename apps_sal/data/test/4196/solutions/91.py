ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("YES") if fl else print("NO")
import collections
import math
import itertools
import heapq as hq
gcd = math.gcd
n = ni()
A = lma()
gcd_l = [1]*n
gcd_l[0]=A[0]
gcd_r =[1]*n
gcd_r[-1] = A[-1]
for i in range(1,n):
    gcd_l[i] = gcd(A[i],gcd_l[i-1])
    gcd_r[-i-1] = gcd(A[-i-1],gcd_r[-i])
ans = max(gcd_l[-2],gcd_r[1])
for i in range(1,n-1):
    ggg = gcd(gcd_l[i-1],gcd_r[i+1])
    ans = max(ans,ggg)
print(ans)

