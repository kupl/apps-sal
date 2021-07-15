import heapq
n,m = map(int,input().split())
a = list(map(int,input().split()))

a = list(map(lambda x:(-1)*x,a))

heapq.heapify(a)

for i in range(m):
    tmp = heapq.heappop(a)
    heapq.heappush(a,(-1)*(((-1)*tmp)//2))
print(sum(a)*(-1))
