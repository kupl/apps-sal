def gns():
    return list(map(int, input().split()))


r, c = gns()
m = [[0] * c for i in range(r)]
rm, cm = [0] * r, [0] * c
for i in range(r):
    x = input()
    for j in range(c):
        if x[j] == '*':
            m[i][j] = 1
            rm[i] += 1
            cm[j] += 1
x, y = 0, 0
for i in range(r):
    if rm[i] >= 3:
        x = i
for j in range(c):
    if cm[j] >= 3:
        y = j
ans = 1
if (x == 0 or x == r - 1 or y == 0 or y == c - 1) or m[x][y] + m[x - 1][y] + m[x + 1][y] + m[x][y - 1] + m[x][y + 1] < 5:
    print('NO')
    quit()
j = y - 1
while j >= 0:
    if m[x][j] == 1:
        ans += 1
    else:
        break
    j -= 1
j = y + 1
while j < c:
    if m[x][j] == 1:
        ans += 1
    else:
        break
    j += 1
i = x - 1
while i >= 0:
    if m[i][y] == 1:
        ans += 1
    else:
        break
    i -= 1
i = x + 1
while i < r:
    if m[i][y] == 1:
        ans += 1
    else:
        break
    i += 1
if ans == sum(rm):
    print('YES')
else:
    print('NO')
