n, m = map(int, input().split())
l = []
for i in range(n):
    l.append(input())
# print(l)
xstart = -1
ystart = -1
xend = -1
yend = -1
for i in range(n):
    for j in range(m):
        if(l[i][j] == 'B' and xstart == -1):
            xstart = j
        if(l[i][j] == 'B' and not(xstart == -1)):
            xend = j
        if(l[i][j] == 'B' and ystart == -1):
            ystart = i
        if(l[i][j] == 'B' and not(ystart == -1)):
            yend = i
print((ystart + yend) // 2 + 1, (xstart + xend) // 2 + 1)
