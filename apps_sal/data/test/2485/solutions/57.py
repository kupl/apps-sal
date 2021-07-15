from collections import defaultdict

h, w, m = map(int, input().split())

rowsum = [0] * h
rowmax = 0
colsum = [0] * w
colmax = 0
targets = defaultdict(int)
for _ in range(m):
    hi, wi = map(int, input().split())
    hi -= 1
    wi -= 1
    rowsum[hi] += 1
    rowmax = max(rowmax, rowsum[hi])
    colsum[wi] += 1
    colmax = max(colmax, colsum[wi])
    targets[(hi, wi)] = 1

rowindices = []
for i, v in enumerate(rowsum):
    if v == rowmax:
        rowindices.append(i)

colindices = []
for i, v in enumerate(colsum):
    if v == colmax:
        colindices.append(i)

ans = rowmax + colmax - 1
for ri in rowindices:
    for ci in colindices:
        if targets[(ri, ci)]:
            continue
        print(rowmax + colmax)
        return

print(ans)
