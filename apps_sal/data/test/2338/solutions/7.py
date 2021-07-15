from bisect import bisect_left as bl, bisect_right as br, insort
import sys
import heapq
#from math import *
from collections import defaultdict as dd, deque
def data(): return sys.stdin.readline().strip()
def mdata(): return list(map(int, data().split()))
#sys.setrecursionlimit(100000)


n=int(data())
A=[]
ans=[]
d=dd(list)
for i in range(n):
    x,y=mdata()
    A.append((x,y))
A.sort(key=lambda x:abs(x[0])+abs(x[1]))
for i in A:
    x,y=i
    if x > 0:
        ans.append('1 %d R' % x)
    elif x < 0:
        ans.append('1 %d L' % -x)
    if y > 0:
        ans.append('1 %d U' % y)
    elif y < 0:
        ans.append('1 %d D' % -y)
    ans.append('2')
    if x > 0:
        ans.append('1 %d L' % x)
    elif x < 0:
        ans.append('1 %d R' % -x)
    if y > 0:
        ans.append('1 %d D' % y)
    elif y < 0:
        ans.append('1 %d U' % -y)
    ans.append('3')
print(len(ans))
print('\n'.join(ans))



