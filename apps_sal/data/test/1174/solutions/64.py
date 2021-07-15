import heapq
n,m = list(map(int,input().split()))
cost = list(map(int,input().split()))
cost = list([x*(-1) for x in cost])
heapq.heapify(cost)

while m != 0 :
    max = heapq.heappop(cost)
    val = ((-1)*max//2)*(-1)
    m -= 1
    heapq.heappush(cost,val)

cost = list([x*(-1) for x in cost])
print((sum(cost)))

