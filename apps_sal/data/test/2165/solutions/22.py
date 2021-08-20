import sys
from operator import lt, gt, le, ge, itemgetter
(n, t) = list(map(int, input().split()))
a = list(zip(list(map(int, input().split())), list(map(int, input().split()))))
nume = sum((a[i][0] * a[i][1] for i in range(n)))
deno = sum((a[i][0] for i in range(n)))
if nume / deno > t:
    (op1, op2, rev) = (gt, le, False)
else:
    (op1, op2, rev) = (lt, ge, True)
a.sort(key=itemgetter(1), reverse=rev)
while len(a) > 1 and op1((nume - a[-1][0] * a[-1][1]) / (deno - a[-1][0]), t):
    nume -= a[-1][0] * a[-1][1]
    deno -= a[-1][0]
    a.pop()
nume -= a[-1][0] * a[-1][1]
deno -= a[-1][0]
(ok, ng) = (0.0, float(a[-1][0]))
for _ in range(50):
    mid = (ok + ng) / 2
    if op2((nume + mid * a[-1][1]) / (deno + mid), t):
        ok = mid
    else:
        ng = mid
print(deno + ok)
