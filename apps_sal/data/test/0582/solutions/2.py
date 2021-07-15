import sys
import heapq
from collections import defaultdict
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
cost=list(map(int,sys.stdin.readline().split()))
for i in range(n):
    arr[i]=[arr[i],cost[i]]
arr.sort()
l=[]
heapq.heapify(l)
prev=0
ans=0
s=0
#print(arr,'arr')
for i in range(n):
    #print(l,'l',s,ans)
    while l and prev<arr[i][0]:
        s-=(l[0])
        ans+=(-s)
        prev+=1
        heapq.heappop(l)
    prev=arr[i][0]
    s+=(-arr[i][1])
    heapq.heappush(l,-arr[i][1])
while l:
    s-=(l[0])
    ans+=(-s)
    heapq.heappop(l)
print(ans)

