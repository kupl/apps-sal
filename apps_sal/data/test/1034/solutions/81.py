
import heapq
import itertools
from collections import defaultdict

x, y, z, k = list(map(int, input().split()))

A = list(int(a) for a in input().split())
B = list(int(b) for b in input().split())
C = list(int(c) for c in input().split())

A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

hq = []
hqAns = []
d = defaultdict(int)

heapq.heappush(hq, ((A[0] + B[0] + C[0]) * -1, (0, 0, 0)))
d[(0, 0, 0)] = 1

while len(hqAns) < k:
    val, key = heapq.heappop(hq)
    heapq.heappush(hqAns, val)

    if d[(key[0] + 1, key[1], key[2])] == 0 and key[0] + 1 < x:
        heapq.heappush(hq, ((A[key[0] + 1] + B[key[1]] + C[key[2]]) * -1, ((key[0] + 1, key[1], key[2]))))
        d[(key[0] + 1, key[1], key[2])] = 1

    if d[(key[0], key[1] + 1, key[2])] == 0 and key[1] + 1 < y:
        heapq.heappush(hq, ((A[key[0]] + B[key[1] + 1] + C[key[2]]) * -1, ((key[0], key[1] + 1, key[2]))))
        d[(key[0], key[1] + 1, key[2])] = 1

    if d[(key[0], key[1], key[2] + 1)] == 0 and key[2] + 1 < z:
        heapq.heappush(hq, ((A[key[0]] + B[key[1]] + C[key[2] + 1]) * -1, ((key[0], key[1], key[2] + 1))))
        d[(key[0], key[1], key[2] + 1)] = 1

for i in range(k):
    print((heapq.heappop(hqAns) * -1))

'''

A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

hq = []
for i in range(x):
    for j in range(y):
        for l in range(z):
            if (i+1)*(j+1)*(l+1)<=k:
                heapq.heappush(hq, (A[i]+B[j]+C[l])*-1)
            else:
                break

for _ in range(k):
    print(heapq.heappop(hq)*-1)

'''

'''


hq = []
for i, j in itertools.product(A, B):
    heapq.heappush(hq, (i+j)*-1)

AB = []
while len(hq)>0 and len(AB)<=k:
    AB.append(heapq.heappop(hq)*-1)

hq = []
for i, j in itertools.product(AB, C):
    heapq.heappush(hq, (i+j)*-1)

for _ in range(k):
    print(heapq.heappop(hq)*-1)

'''
