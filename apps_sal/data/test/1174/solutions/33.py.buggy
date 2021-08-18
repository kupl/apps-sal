import heapq
n, m = map(int, input().split())
a = list(map(int, input().split()))
if n == 1:
    print(a[0] // (2 ** m))
    return
a = list(map(lambda x: x * (-1), a))
heapq.heapify(a)
while m > 0:
    m -= 1
    i = heapq.heappop(a) * (-1)
    i //= 2
    heapq.heappush(a, i * (-1))

print(sum(a) * (-1))
