from heapq import *

a = [*list(range(1, 10))]
heapify(a)
i = 0
k = int(input())
c = 0
while True:
    t = str(heappop(a))
    i += 1
    if i == k:
        break
    if t[-1] != "0":
        heappush(a, int(t + str(int(t[-1]) - 1)))
    heappush(a, int(t + t[-1]))
    if t[-1] != "9":
        heappush(a, int(t + str(int(t[-1]) + 1)))
print(t)
