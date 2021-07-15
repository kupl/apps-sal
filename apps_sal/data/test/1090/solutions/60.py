import sys
import heapq
import math
import fractions
import bisect
import itertools
from collections import Counter
from collections import deque
from operator import itemgetter
def input(): return sys.stdin.readline().strip()
def mp(): return list(map(int,input().split()))
def lmp(): return list(map(int,input().split()))

n,k=mp()
s=list(input())
ans=[]
c=1
for i in range(1,n):
    if s[i]==s[i-1]:
        c+=1
    else:
        ans.append(c)
        c=1
ans.append(c)
if len(ans)//2<=k:
    print((n-1))
else:
    print((n-len(ans)+2*k))

