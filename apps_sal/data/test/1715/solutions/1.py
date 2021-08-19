import bisect
import math
(a, b, q) = map(int, input().split())
s = [-math.inf]
t = [-math.inf]
x = []
for _ in range(a):
    s.append(int(input()))
for _ in range(b):
    t.append(int(input()))
for _ in range(q):
    x.append(int(input()))
s.append(math.inf)
t.append(math.inf)
for i in x:
    ws = abs(s[bisect.bisect(s, i) - 1] - i)
    if ws != math.inf:
        ws += min(abs(t[bisect.bisect(t, s[bisect.bisect(s, i) - 1]) - 1] - s[bisect.bisect(s, i) - 1]), abs(t[bisect.bisect(t, s[bisect.bisect(s, i) - 1])] - s[bisect.bisect(s, i) - 1]))
    else:
        ws = math.inf
    es = abs(s[bisect.bisect(s, i)] - i)
    if es != math.inf:
        es += min(abs(t[bisect.bisect(t, s[bisect.bisect(s, i)]) - 1] - s[bisect.bisect(s, i)]), abs(t[bisect.bisect(t, s[bisect.bisect(s, i)])] - s[bisect.bisect(s, i)]))
    else:
        es = math.inf
    wt = abs(t[bisect.bisect(t, i) - 1] - i)
    if wt != math.inf:
        wt += min(abs(s[bisect.bisect(s, t[bisect.bisect(t, i) - 1]) - 1] - t[bisect.bisect(t, i) - 1]), abs(s[bisect.bisect(s, t[bisect.bisect(t, i) - 1])] - t[bisect.bisect(t, i) - 1]))
    else:
        wt = math.inf
    et = abs(t[bisect.bisect(t, i)] - i)
    if et != math.inf:
        et += min(abs(s[bisect.bisect(s, t[bisect.bisect(t, i)]) - 1] - t[bisect.bisect(t, i)]), abs(s[bisect.bisect(s, t[bisect.bisect(t, i)])] - t[bisect.bisect(t, i)]))
    else:
        et = math.inf
    print(min(ws, es, wt, et))
