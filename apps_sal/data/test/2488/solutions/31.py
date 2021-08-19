from math import *
from collections import *
(N, D, A) = list(map(int, input().split()))
ans = 0
t = 0
q = deque()
XH = sorted([list(map(int, input().split())) for i in range(N)])
for (x, h) in XH:
    if q:
        while q and q[0][0] < x - D:
            (_, c) = q.popleft()
            t -= c
    h = h - t * A
    if h <= 0:
        continue
    x += D
    c = ceil(h / A)
    t += c
    ans += c
    q.append((x, c))
print(ans)
