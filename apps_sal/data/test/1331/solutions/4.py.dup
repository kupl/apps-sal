from collections import deque
n, m, k = (int(x) for x in input().split())
ns = set((int(x) for x in input().split()))
span = deque((0 for i in range(m)))
kk = 0
res = 0
mm = -1
while len(ns) > 0:
    mm += 1
    x = span.popleft()
    if x == 1:
        kk -= 1
    if mm not in ns:
        span.append(0)
    else:
        ns.remove(mm)
        y = 1
        if kk == k - 1:
            res += 1
            y = 0
        span.append(y)
        kk += y
print(res)
