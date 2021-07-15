import heapq
n,m=map(int,input().split())
a=list(map(int,input().split()))

a=[-i for i in a]
heapq.heapify(a)
for _ in range(m):
     b=heapq.heappop(a)
     heapq.heappush(a,-((-b)//2))

print(-sum(a))
