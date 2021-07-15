n,m = list(map(int,input().split()))
dic = {}
for i in range(n):
    dic[i] = input()
first = False
for i in range(n):
    for j in range(m):
        if dic[i][j] == 'X':
            corner1 = (i,j)
            first = True
            break
    if first:
        break
for i in range(corner1[0],n+1):
    if i == n or dic[i][corner1[1]] == '.':
        corner2 = i-1
        break
for i in range(corner1[1],m+1):
    if i == m or dic[corner1[0]][i] == '.':
        corner3 = i-1
        break
rec = True
for i in range(n):
    for j in range(m):
        if i < corner1[0] or i > corner2 or j <corner1[1] or j > corner3:
            if dic[i][j] == 'X':
                rec = False
                break
        else:
            if dic[i][j] == '.':
                rec = False
                break
if rec:
    print("YES")
else:
    print("NO")

