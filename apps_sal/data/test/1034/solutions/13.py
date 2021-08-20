import heapq
import itertools
(x, y, z, k) = list(map(int, input().split()))
A = list((int(a) for a in input().split()))
B = list((int(b) for b in input().split()))
C = list((int(c) for c in input().split()))
A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)
hq = []
for i in range(x):
    for j in range(y):
        for l in range(z):
            if (i + 1) * (j + 1) * (l + 1) <= k:
                heapq.heappush(hq, (A[i] + B[j] + C[l]) * -1)
            else:
                break
'\nhq = []\nfor i, j in itertools.product(A, B):\n    heapq.heappush(hq, (i+j)*-1)\n\nAB = []\nwhile len(hq)>0 and len(AB)<=k:\n    AB.append(heapq.heappop(hq)*-1)\n\nhq = []\nfor i, j in itertools.product(AB, C):\n    heapq.heappush(hq, (i+j)*-1)\n'
for _ in range(k):
    print(heapq.heappop(hq) * -1)
