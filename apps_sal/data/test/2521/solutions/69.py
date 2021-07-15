import heapq
n=int(input())
a=[int(i) for i in input().split()]
 
heap_left=[]
left=0
for i in range(n):
    left+=a[i]
    heapq.heappush(heap_left,a[i])
 
lst_left=[left]
for i in range(n,2*n):
    tmp=heapq.heappushpop(heap_left,a[i])
    left=left-tmp+a[i]
    lst_left+=[left]
 
heap_right=[]
right=0
for i in range(2*n,3*n):
    right+=a[i]
    heapq.heappush(heap_right,-a[i])
 
lst_right=[right]
for i in range(2*n-1,n-1,-1):
    tmp=heapq.heappushpop(heap_right,-a[i])
    right=right-(-tmp)+a[i]
    lst_right+=[right]
 

ans=-10**100
for i in range(n+1):
    ans=max(ans,lst_left[i]-lst_right[-(i+1)])
 
print (ans)
