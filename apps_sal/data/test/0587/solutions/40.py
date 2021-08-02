from collections import Counter
from heapq import heappush, heappop

n, k = list(map(int, input().split()))
s = []
for _ in range(n):
    t, d = list(map(int, input().split()))
    s.append((d, t))
s.sort()
bp = 0
x = 0
c = Counter()
cand = []
for _ in range(k):
    d, t = s.pop()
    bp += d
    if c[t] == 0:
        x += 1
    c[t] += 1
    heappush(cand, (d, t))
ans = bp + x * x
while s:
    d, t = s.pop()
    if c[t] == 0:
        while cand:
            dd, td = heappop(cand)
            if c[td] == 1:
                continue
            else:
                c[td] -= 1
                bp -= dd
                break
        else:
            break
        bp += d
        x += 1
        c[t] = 1
        ans = max(ans, bp + x * x)
print(ans)
