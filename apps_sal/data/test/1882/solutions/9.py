import sys
import math
from collections import defaultdict,deque
import heapq
def search(arr,points,t):
    l=[]
    n=len(arr)
    cnt=0
    for i in range(n):
        if arr[i][0]>=points:
            l.append(arr[i][1])
            cnt+=1
    if cnt>=points:
        l.sort()
        #print(l,'l')
        if sum(l[:points])<=t:
            return True
    return False
def get(arr,points):
    n=len(arr)
    l=[]
    for i in range(n):
        if arr[i][0]>=points:
            l.append([arr[i][1],arr[i][2]+1])
    l.sort()
    #print(l,'get')
    res=[]
    for i in range(points):
        res.append(l[i][1])
    return res
n,t=list(map(int,sys.stdin.readline().split()))
dic=defaultdict(int)
arr=[]
for i in range(n):
    a,b=list(map(int,sys.stdin.readline().split()))
    arr.append([a,b,i])
low,high=0,n
ans=0
while low<=high:
    mid=(low+high)//2
    if search(arr,mid,t):
        ans=max(ans,mid)
        low=mid+1
    else:
        high=mid-1
#print(ans)
if ans==0:
    print(0)
    print(0)
    print('')
    return
l=get(arr,ans)
print(len(l))
print(len(l))
print(*l)


