from collections import defaultdict
import bisect
s, t = [x.strip() for x in open(0).readlines()]
if set(t) - set(s) != set():
    print(-1)
else:
    d = defaultdict(list)
    n = len(s)
    for i, c in enumerate(s, 1):
        d[c].append(i)
    for k in d:
        d[k].append(d[k][0] + n)
    ans = 0
    for c in t:
        q, r = divmod(ans, n)
        x = d[c][bisect.bisect(d[c], r)]
        ans = n * q + x
    print(ans)
