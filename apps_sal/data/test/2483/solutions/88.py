from collections import defaultdict as dd
(N, C) = tuple(map(int, input().split()))
events = []
tmax = 0
dic = dd(list)
for i in range(N):
    (s, t, c) = map(int, input().split())
    dic[c].append((s, t))
eps = 0.5
for (k, v) in dic.items():
    v1 = sorted(v)
    lev = len(v1)
    prev = [-1, -1]
    for (i, val) in enumerate(v1):
        if tmax < val[1]:
            tmax = val[1]
        if prev == [-1, -1]:
            prev[0] = val[0]
            prev[1] = val[1]
            if lev != 1:
                continue
            else:
                events.append((prev[0] - eps, 1))
                events.append((prev[1], 0))
                break
        if prev[1] == val[0]:
            prev[1] = val[1]
            if i == lev - 1:
                events.append((prev[0] - eps, 1))
                events.append((prev[1], 0))
                break
        else:
            events.append((prev[0] - eps, 1))
            events.append((prev[1], 0))
            prev[0] = val[0]
            prev[1] = val[1]
            if i == lev - 1:
                events.append((val[0] - eps, 1))
                events.append((val[1], 0))
                break
events.sort()
idx = 0
cnt = 0
res = 0
events.append((0, -1))
for t in range(tmax + 1):
    while events[idx][0] <= t:
        event = events[idx]
        if event[1] == 1:
            cnt += 1
            if res < cnt:
                res = cnt
        elif event[1] == 0:
            cnt -= 1
        else:
            break
        idx += 1
print(res)
