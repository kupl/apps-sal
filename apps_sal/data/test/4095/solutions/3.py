from collections import defaultdict

n, m = list(map(int, input().split()))
ls = [int(i) for i in input().split()]

pos = 0
for i, j in enumerate(ls):
    if j == m:
        pos = i
        break

cnt = 1

L = defaultdict(int)
R = defaultdict(int)

upper, lower = 0, 0

for i in range(pos-1, -1, -1):
    if ls[i] > m:
        upper += 1
    else:
        lower += 1

    if upper == lower or upper - lower == 1:
        cnt += 1

    L[lower - upper] += 1


upper, lower = 0, 0

for i in range(pos+1, n):
    if ls[i] > m:
        upper += 1
    else:
        lower += 1

    if upper == lower or upper - lower == 1:
        cnt += 1

    R[lower - upper] += 1


for i in list(L.keys()):
    cnt += L[i] * R[-i]
    cnt += L[i] * R[-i-1]

print(cnt)

