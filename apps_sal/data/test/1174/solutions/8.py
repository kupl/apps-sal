import heapq
N,M=map(int,input().split())
A=list(map(lambda x:int(x)*(-1),input().split()))

heapq.heapify(A)

for _ in range(M):
    tmp=heapq.heappop(A)
    tmp=-tmp//2
    heapq.heappush(A,-tmp)

print(-sum(A))
