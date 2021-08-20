(n, m) = map(int, input().split())
a = []
array = []
for i in range(n):
    a.append(list(map(str, input())))
    listt = []
    for c in range(m):
        if a[i][c] == '#':
            listt.append(1)
        else:
            listt.append(0)
    array.append(listt)
for y in range(1, n - 1):
    for x in range(1, m - 1):
        f = a[y + 1][x] == '#' and a[y + 1][x + 1] == '#' and (a[y + 1][x - 1] == '#')
        s = a[y][x + 1] == '#' and a[y][x - 1] == '#'
        th = a[y - 1][x] == '#' and a[y - 1][x + 1] == '#' and (a[y - 1][x - 1] == '#')
        if f and s and th:
            array[y + 1][x] -= 1
            array[y + 1][x + 1] -= 1
            array[y + 1][x - 1] -= 1
            array[y][x + 1] -= 1
            array[y][x - 1] -= 1
            array[y - 1][x - 1] -= 1
            array[y - 1][x] -= 1
            array[y - 1][x + 1] -= 1
mb = True
for y in range(n):
    for x in range(m):
        if array[y][x] == 1:
            mb = False
            break
if mb:
    print('YES')
else:
    print('NO')
