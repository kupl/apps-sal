import math
from itertools import permutations
N=int(input())
XYlist=[]
indexlist=[i for i in range(N)]
for _ in range(N):
    XYlist.append(tuple(map(int,input().split())))
ans=0
num=0
for indexes in permutations(indexlist,N):
    for i in range(N-1):
        ans+=math.sqrt((XYlist[indexes[i]][0]-XYlist[indexes[i+1]][0])**2+
                       (XYlist[indexes[i]][1]-XYlist[indexes[i+1]][1])**2)
    num+=1
print(ans/num)
