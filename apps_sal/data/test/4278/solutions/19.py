import math
N = int(input())
records = {}
for i in range(N):
    l = ''.join(sorted(input()))
    records.setdefault(l, 0)
    records[l] += 1
count = 0
for v in records.values():
    if v == 1:
        continue
    else:
        count += math.comb(v, 2)
print(count)
