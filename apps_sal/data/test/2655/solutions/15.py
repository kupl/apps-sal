import heapq
n = int(input())
a = list(map(int, input().split()))
a = list([x * -1 for x in a])
heapq.heapify(a)
total = 0
total += -1 * heapq.heappop(a)
if n % 2 == 1:
    for i in range(1, n // 2 + 1):
        if i == n // 2:
            total += -1 * heapq.heappop(a)
        else:
            total += -2 * heapq.heappop(a)
    print(total)
else:
    for i in range(1, n // 2):
        total += -2 * heapq.heappop(a)
    print(total)
