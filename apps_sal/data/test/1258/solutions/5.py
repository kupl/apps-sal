import sys
from collections import defaultdict
n = int(input())
count = [0] * (n + 1)
d = defaultdict(list)
di = 10 ** 6
for (q1, q2, q3) in (list(map(int, l.split())) for l in sys.stdin):
    count[q1] += 1
    count[q2] += 1
    count[q3] += 1
    d[q1 * di + q2 if q1 < q2 else q2 * di + q1].append(q3)
    d[q1 * di + q3 if q1 < q3 else q3 * di + q1].append(q2)
    d[q2 * di + q3 if q2 < q3 else q3 * di + q2].append(q1)
(i1, i2) = ([], [])
for i in range(1, n + 1):
    if count[i] == 1:
        i1.append(i)
    elif count[i] == 2:
        i2.append(i)
key = []
ans = [0] * n
if (i1[0] * di + i2[0] if i1[0] < i2[0] else i2[0] * di + i1[0]) in d:
    key = [i1[0], i2[0]]
else:
    key = [i1[0], i2[1]]
(ans[0], ans[1]) = (key[0], key[1])
used = {key[0], key[1]}
for i in range(2, n):
    next_key = key[0] * di + key[1] if key[0] < key[1] else key[1] * di + key[0]
    next_l = d[next_key]
    next_n = next_l[0] if next_l[0] not in used else next_l[1]
    ans[i] = next_n
    (key[0], key[1]) = (key[1], next_n)
    used.add(next_n)
print(*ans)
