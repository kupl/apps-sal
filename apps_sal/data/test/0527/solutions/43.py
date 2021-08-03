from bisect import bisect_left as bisect
from collections import defaultdict


s, t = input(), input()
lens, sets = len(s), set(s)

if not all(i in sets for i in t):
    print((-1))
    return

alp = defaultdict(list)
for i, si in enumerate(s):
    alp[si].append(i)

ans, cnt = 1 - lens, 0
for i in t:
    ans += lens * (cnt == 0)
    num = bisect(alp[i], cnt)
    ans += lens * (num == len(alp[i]))
    cnt = (alp[i][num % len(alp[i])] + 1) % lens
print((ans + (cnt - 1) % lens))
