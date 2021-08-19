import heapq as hq
from queue import PriorityQueue
import math
(n, m, r, k) = input().split()
N = int(n)
M = int(m)
R = int(r)
K = int(k)
q = PriorityQueue()
for i in range(1, math.floor((N + 1) / 2) + 1):
    maxi = min(min(i, N - i + 1), min(R, N - R + 1)) * min(min(R, M - R + 1), math.ceil(M / 2))
    num = M - (2 * min(min(R, M - R + 1), math.ceil(M / 2)) - 2)
    mult = 2
    if i > math.floor(N / 2):
        mult = 1
    q.put((-maxi, num * mult, i))
ans = 0
while K > 0:
    pop = q.get()
    a = -1 * pop[0]
    b = pop[1]
    c = pop[2]
    d = min(min(c, N - c + 1), min(R, N - R + 1))
    if d != a:
        mult = 2
        if c > N / 2:
            mult = 1
        q.put((-(a - d), 2 * mult, c))
    ans += a * min(b, K)
    K -= b
tot = (N - R + 1) * (M - R + 1)
print(str(ans / tot))
'\n\nd = []\nfor i in range(0,N):\n    d.append([])\n    for j in range(0,M):\n        d[i].append(0)\n\ntot = 0\nfor i in range(0,N-R+1):\n    for j in range(0,M-R+1):\n        for k in range(i,i+R):\n            for l in range(j,j+R):\n                d[k][l] += 1\n                tot += 1\n\n\nprint(N-R+1)*(M-R+1) * (R*R)\nprint(tot)\nprint()\nfor i in d:\n    print(i)\n\n'
