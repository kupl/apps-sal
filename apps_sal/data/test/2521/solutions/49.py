import sys
from heapq import heapify, heappop, heappush
read = sys.stdin.read
(N, *a) = list(map(int, read().split()))
a1 = a[:N]
a2 = a[N:-N]
a3 = a[-N:]
left = sum(a1)
right = sum(a3)
heapify(a1)
a3 = [-i for i in a3]
heapify(a3)
b = [0] * (N + 1)
b[0] = left
for (n, i) in enumerate(a2, 1):
    if a1[0] < i:
        j = heappop(a1)
        left = left - j + i
        heappush(a1, i)
    b[n] = left
c = [0] * (N + 1)
c[0] = right
for (n, i) in enumerate(a2[::-1], 1):
    if i < -a3[0]:
        j = -heappop(a3)
        right = right - j + i
        heappush(a3, -i)
    c[n] = right
c = c[::-1]
answer = max((i - j for (i, j) in zip(b, c)))
print(answer)
