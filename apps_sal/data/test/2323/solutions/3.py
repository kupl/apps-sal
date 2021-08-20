import sys
import bisect
n = int(input())
s = sorted([int(x) for x in input().split(' ')])
dif = sorted([s[i + 1] - s[i] for i in range(0, n - 1)])
adif = []
if n > 1:
    adif.append(dif[0])
    for i in range(1, len(dif)):
        adif.append(adif[-1] + dif[i])
q = int(input())
res = []
for i in range(q):
    line = input().split(' ')
    l = int(line[0])
    r = int(line[1])
    span = r - l + 1
    idx = bisect.bisect_right(dif, span) - 1
    if idx >= 0:
        acc_diff = adif[idx]
        ans = n * span - ((idx + 1) * span - acc_diff)
    else:
        ans = n * span
    res.append(ans)
print(str(' '.join((str(x) for x in res))))
