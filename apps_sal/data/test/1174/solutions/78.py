import heapq
n,m=map(int,input().split())
a=list(map(lambda x:-int(x),input().split()))
heapq.heapify(a)
for i in range(m):
    x=-heapq.heappop(a)
    heapq.heappush(a,-(x//2))
print(-sum(a))
