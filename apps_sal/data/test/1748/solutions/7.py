from heapq import *
n = int(input())
l = list(map(int, input().split()))
l1 = list(map(int, input().split()))
L = []
heapify(L)
l2 = l1[:]
qw = []
for i in range(1, n):
    l2[i] += l2[i - 1]
for i in range(n):
    v = l[i] + l2[i] - l1[i]
    heappush(L, v)
    mi = heappop(L)
    count = 0
    while mi <= l2[i]:
        count += mi - l2[i] + l1[i]
        if not L:
            break
        mi = heappop(L)
    else:
        heappush(L, mi)
    ost = count + len(L) * l1[i]
    qw.append(ost)
print(*qw)
