from collections import defaultdict
from operator import itemgetter
n = int(input().strip())
p = list(map(int, input().strip().split()))
ml = -float('inf')
mli = None
ms = -float('inf')
msi = None
count = defaultdict(int)
isRecord = [0] * n
for (i, v) in enumerate(p):
    if v > ml:
        isRecord[i] = 1
    if ms < v <= ml:
        count[mli] += 1
    if v >= ml:
        (ms, msi) = (ml, mli)
        (ml, mli) = (v, i)
    elif v >= ms:
        (ms, msi) = (v, i)
num = sum(isRecord)
ma = -float('inf')
mai = None
for i in range(n):
    v = count[i] - isRecord[i] + num
    if v > ma:
        ma = v
        mai = i
    elif v == ma and p[i] < p[mai]:
        mai = i
print(p[mai])
