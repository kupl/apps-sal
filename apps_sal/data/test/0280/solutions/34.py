import sys, math
import io, os
#data = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
from bisect import bisect_left as bl, bisect_right as br, insort
from heapq import heapify, heappush, heappop
from collections import defaultdict as dd, deque, Counter
from itertools import permutations,combinations
def data(): return sys.stdin.readline().strip()
def mdata(): return list(map(int, data().split()))
def outl(var) : sys.stdout.write('\n'.join(map(str, var))+'\n')
def out(var) : sys.stdout.write(str(var)+'\n')
#from decimal import Decimal
#from fractions import Fraction
#sys.setrecursionlimit(100000)
INF = float('inf')
mod = int(1e9)+7


n,m=mdata()
w=mdata()
part=sorted([mdata() for i in range(m)],key=lambda x:x[1])
part1=[part[0][1]]
part2=[0,part[0][0]]
for i in range(1,m):
    part1.append(part[i][1])
    part2.append(max(part2[-1],part[i][0]))
if min(part1)<max(w):
    out(-1)
    return
perm=list(permutations(w))
ans=INF
for lis in perm:
    dp=[0]*n
    for i in range(n):
        ind=i
        k=lis[i]
        for j in range(i+1,n):
            k+=lis[j]
            dp[j]=max(dp[j],dp[i]+part2[bl(part1,k)])
    ans=min(ans,dp[-1])
out(ans)
