(n, k) = [int(i) for i in input().split()]
sz = n - k + 1
cnt = []
for i in range(sz):
    cnt.append([0] * sz)
data = []
extra = 0
for i in range(n):
    data.append(input())
for r in range(n):
    row = data[r]
    li = row.find('B')
    if li == -1:
        extra += 1
        continue
    ri = row.rfind('B')
    for i in range(max(ri - k + 1, 0), min(li + 1, sz)):
        for j in range(max(0, r + 1 - k), min(sz, r + 1)):
            cnt[j][i] += 1
for c in range(n):
    row = ''.join([data[i][c] for i in range(n)])
    li = row.find('B')
    if li == -1:
        extra += 1
        continue
    ri = row.rfind('B')
    for i in range(max(ri - k + 1, 0), min(li + 1, sz)):
        for j in range(max(0, c + 1 - k), min(sz, c + 1)):
            cnt[i][j] += 1
mx = 0
for i in range(sz):
    for j in range(sz):
        if cnt[i][j] > mx:
            mx = cnt[i][j]
print(mx + extra)
