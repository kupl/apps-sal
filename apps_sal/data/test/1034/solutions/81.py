import heapq
import itertools
from collections import defaultdict
(x, y, z, k) = list(map(int, input().split()))
A = list((int(a) for a in input().split()))
B = list((int(b) for b in input().split()))
C = list((int(c) for c in input().split()))
A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)
hq = []
hqAns = []
d = defaultdict(int)
heapq.heappush(hq, ((A[0] + B[0] + C[0]) * -1, (0, 0, 0)))
d[0, 0, 0] = 1
while len(hqAns) < k:
    (val, key) = heapq.heappop(hq)
    heapq.heappush(hqAns, val)
    if d[key[0] + 1, key[1], key[2]] == 0 and key[0] + 1 < x:
        heapq.heappush(hq, ((A[key[0] + 1] + B[key[1]] + C[key[2]]) * -1, (key[0] + 1, key[1], key[2])))
        d[key[0] + 1, key[1], key[2]] = 1
    if d[key[0], key[1] + 1, key[2]] == 0 and key[1] + 1 < y:
        heapq.heappush(hq, ((A[key[0]] + B[key[1] + 1] + C[key[2]]) * -1, (key[0], key[1] + 1, key[2])))
        d[key[0], key[1] + 1, key[2]] = 1
    if d[key[0], key[1], key[2] + 1] == 0 and key[2] + 1 < z:
        heapq.heappush(hq, ((A[key[0]] + B[key[1]] + C[key[2] + 1]) * -1, (key[0], key[1], key[2] + 1)))
        d[key[0], key[1], key[2] + 1] = 1
for i in range(k):
    print(heapq.heappop(hqAns) * -1)
'\n# ans.2 #\n\nA.sort(reverse=True)\nB.sort(reverse=True)\nC.sort(reverse=True)\n\nhq = []\nfor i in range(x):\n    for j in range(y):\n        for l in range(z):\n            if (i+1)*(j+1)*(l+1)<=k:\n                heapq.heappush(hq, (A[i]+B[j]+C[l])*-1)\n            else:\n                break\n\nfor _ in range(k):\n    print(heapq.heappop(hq)*-1)\n\n'
'\n\n# ans.1 #\n\nhq = []\nfor i, j in itertools.product(A, B):\n    heapq.heappush(hq, (i+j)*-1)\n\nAB = []\nwhile len(hq)>0 and len(AB)<=k:\n    AB.append(heapq.heappop(hq)*-1)\n\nhq = []\nfor i, j in itertools.product(AB, C):\n    heapq.heappush(hq, (i+j)*-1)\n\nfor _ in range(k):\n    print(heapq.heappop(hq)*-1)\n\n'
