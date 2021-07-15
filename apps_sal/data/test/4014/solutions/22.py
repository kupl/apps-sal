# from itertools import accumulate
# from bisect import bisect_left
# from collections import OrderedDict

I = lambda: list(map(int, input().split()))

n, m = I()
dates = [0 for i in range(n + 1)]
data = []
for i in range(m):
    d = I() + [i + 1]
    if dates[d[1]]:
        print(-1)
        return
    dates[d[1]] = m + 1
    data.append(d)
data.sort(key = lambda x: x[1])
for s, d, c, idx in data:
    x = 0
    for i in range(s, d):
        if x == c:
            break
        if not dates[i]:
            dates[i] = idx
            x += 1
    if x != c:
        print(-1)
        return
print(*dates[1:])
