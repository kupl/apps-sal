import sys
input=sys.stdin.readline
#print=sys.stdout.write
#sys.setrecursionlimit(100000)
#from heapq import *
#from collections import deque as dq
from math import ceil,floor,sqrt,gcd,log
#import bisect as bs
#from collections import Counter
#from collections import defaultdict as dc 
#from functools import reduce
#from functools import lru_cache
ri=lambda:int(input())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
for _ in range(1):
    N=ri()
    ans=1
    for i in range(2,N+1):
        ans=ans*i//gcd(ans,i)
    print(ans+1)
