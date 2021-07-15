import heapq

x,y,z,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

a.sort(reverse=True)
b.sort(reverse=True)
c.sort(reverse=True)

li = [(-(a[0]+b[0]+c[0]),0,0,0)]

heapq.heapify(li)

for i in range(k):
    ans = heapq.heappop(li)
    print(-ans[0])
    if x > ans[1]+1 and (-(a[ans[1]+1]+b[ans[2]]+c[ans[3]]),ans[1]+1,ans[2],ans[3]) not in li: 
        heapq.heappush(li,(-(a[ans[1]+1]+b[ans[2]]+c[ans[3]]),ans[1]+1,ans[2],ans[3]))
    if y > ans[2]+1 and (-(a[ans[1]]+b[ans[2]+1]+c[ans[3]]),ans[1],ans[2]+1,ans[3]) not in li:
        heapq.heappush(li,(-(a[ans[1]]+b[ans[2]+1]+c[ans[3]]),ans[1],ans[2]+1,ans[3]))
    if z > ans[3]+1 and (-(a[ans[1]]+b[ans[2]]+c[ans[3]+1]),ans[1],ans[2],ans[3]+1) not in li:
        heapq.heappush(li,(-(a[ans[1]]+b[ans[2]]+c[ans[3]+1]),ans[1],ans[2],ans[3]+1))
