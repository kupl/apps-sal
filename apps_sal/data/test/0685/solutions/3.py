import bisect
(n, h) = [int(e) for e in input().split()]
x = [list(map(int, input().split())) for i in range(n)]
xcum = [x[0][1] - x[0][0]]
for (i, e) in enumerate(x[1:]):
    xcum.append(xcum[i] + e[1] - e[0])
x_start = [e[0] for e in x]
i = 0
best = -1
cd = x[0][1] - x[0][0]
ch = h
j = i
while i < len(x):
    while j + 1 < len(x) and x[j][1] + ch > x[j + 1][0]:
        cd += x[j + 1][1] - x[j][1]
        ch -= x[j + 1][0] - x[j][1]
        j += 1
    if cd + ch > best:
        best = cd + ch
    if i + 1 < len(x):
        cd -= x[i + 1][0] - x[i][0]
        ch += x[i + 1][0] - x[i][1]
    i += 1
print(best)
