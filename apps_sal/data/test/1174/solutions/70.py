import heapq

n, m = map(int, input().split())
a = list(map(lambda x: int(x)*(-1), input().split()))
heapq.heapify(a)

while m > 0:
    a_max = heapq.heappop(a)
    if a_max == 0:
        break
    heapq.heappush(a, (-1)*(-a_max // 2))
    m -= 1
print(sum(a)*(-1))
