ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("YES") if fl else print("NO")
import collections
import math
import itertools
import heapq as hq
n = ni()
ab = []
for i in range(n):
    ab.append(lma())
ab.sort(key=lambda x:x[1],reverse=True)
ab.sort(reverse=True)
cd = []
for i in range(n):
    cd.append(lma())
cd.sort()
cd.sort(key=lambda x:x[1])
cnt=0
INF=10**9
for a,b in ab:
    #print("ab",a,b)
    for i in range(n):
        c,d = cd[i]
        if a<c and b<d:
            #print("cd",c,d)
            cnt+=1
            cd[i][0]=-INF
            cd[i][1]=-INF
            break
print(cnt)
#print(cd)

