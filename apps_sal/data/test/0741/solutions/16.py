n, m = map(int, input().strip().split())
l = list(map(int, input().strip().split()))
l.insert(0, 0)
l.append(m)
lc = []
lo = []
on = 0
off = 0
lo.append([0, 0])
for i in range(1, n + 2):
    if (i % 2 == 1):
        on = on + l[i] - l[i - 1]
    else:
        off = off + l[i] - l[i - 1]
    lo.append([on, off])
max1 = on
lc.append([on, off])
for i in range(1, n + 2):
    if (i % 2 == 1):
        on = on - l[i] + l[i - 1]
    else:
        off = off - l[i] + l[i - 1]
    lc.append([on, off])
for i in range(1, n + 2):
    if (i % 1 == 0 and l[i] - l[i - 1] > 1):
        curron = lo[i - 1][0] + l[i] - l[i - 1] - 1 + lc[i][1]
        if (curron > max1):
            max1 = curron
    elif (l[i] - l[i - 1] > 1):
        curron = lo[i - 1][0] + l[i] - 1 - l[i - 1] + lc[i][1]
        if (curron > max1):
            max1 = curron
    else:
        continue
print(max1)
