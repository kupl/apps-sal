from collections import deque
(N, C) = list(map(int, input().split()))
Mx = 10 ** 5 + 1
sch = [[0] * Mx for _ in range(C)]
scht = [0] * Mx
plist = [[] for _ in range(C)]
for _ in range(N):
    (s, t, c) = list(map(int, input().split()))
    plist[c - 1].append((s, t))
for (c, p) in enumerate(plist):
    p.sort()
    prevt = 0
    for (s, t) in p:
        if prevt == s:
            sch[c][prevt] = 0
        else:
            sch[c][s] = 1
        sch[c][t] = -1
        prevt = t
    for i in range(1, Mx):
        if sch[c][i] == 1:
            scht[i - 1] += 1
        if sch[c][i] == -1:
            scht[i] -= 1
for i in range(1, Mx):
    scht[i] += scht[i - 1]
print(max(scht))
