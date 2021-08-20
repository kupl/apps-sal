(n, m) = [int(i) for i in input().split()]
field = []
bomb = []
for i in range(n):
    field.append([])
    data = input()
    count = 0
    for j in data:
        if j == '.':
            j = '0'
        if j == '*':
            bomb.append([i, count])
            j = '-1'
        field[i].append(int(j))
        count += 1
ans = []
for i in range(n):
    ans.append([])
    for j in range(m):
        ans[i].append(0)
directx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
directy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
for i in bomb:
    x = i[0]
    y = i[1]
    ans[x][y] = -1
    for j in range(9):
        x1 = directx[j] + x
        y1 = directy[j] + y
        if 0 <= x1 < n and 0 <= y1 < m:
            if ans[x1][y1] != -1:
                ans[x1][y1] += 1
for i in range(n):
    for j in range(m):
        if ans[i][j] != field[i][j]:
            print('NO')
            quit()
print('YES')
