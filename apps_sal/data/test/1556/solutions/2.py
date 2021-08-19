import heapq

n, k, v = list(map(int, input().split()))
num = list(map(int, input().split()))

sign = len([x for x in num if x < 0])
minx, mini = min([[abs(x), i] for i, x in enumerate(num)])

if sign % 2 == 0:
    if num[mini] < 0:
        c = min(minx // v + 1, k)
        k -= c
        num[mini] += v * c
    elif num[mini] >= 0:
        c = min(minx // v + 1, k)
        k -= c
        num[mini] -= v * c


heap = []
heapq.heapify(heap)
for i, x in enumerate(num):
    heapq.heappush(heap, [abs(x), i])

while k:
    absx, curi = heapq.heappop(heap)
    #print(curi, num[curi])
    if num[curi] >= 0:
        num[curi] += v
    else:
        num[curi] -= v
    heapq.heappush(heap, [abs(num[curi]), curi])
    k -= 1

print(' '.join([str(x) for x in num]))
