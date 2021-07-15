def next1(x, y):
    nonlocal data, ans
    data[y][x][1] = True
    if data[y][x - 1][0] == '*' and ( not data[y][x - 1][1]):
        ans += 'L'
        return x - 1, y
    if data[y - 1][x][0] == '*' and ( not data[y - 1][x][1]):
        ans += 'U'
        return x, y - 1
    if data[y][x + 1][0] == '*' and ( not data[y][x + 1][1]):
        ans += 'R'
        return x + 1, y
    if data[y + 1][x][0] == '*' and ( not data[y + 1][x][1]):
        ans += 'D'
        return x, y + 1
    return None, None
    

n, m = map(int, input().split())
data = []
data.append([])
for i in range(m + 2):
    data[0].append(['.', False])
for i in range(n):
    h = input()
    sd = []
    sd.append(['.', False])
    for i in range(m):
        sd.append([h[i], False])
    sd.append(['.', False])
    data.append(sd)
data.append([])
for i in range(m + 2):
    data[-1].append(['.', False])
f = True
startx, starty = -1, -1
for i in range(1, n + 1):
    if f:
        for j in range(1, m + 1):
            if data[i][j][0] == 'S':
                startx, starty = j, i
                f = False
                break
x, y, h1, h2 = startx, starty, startx, starty
ans = ''
if data[y][x - 1][0] == '*' and ( not data[y][x - 1][1]):
    x, y =  x - 1, y
    ans += 'L'
elif data[y - 1][x][0] == '*' and ( not data[y - 1][x][1]):
    x, y = x, y - 1
    ans += 'U'
elif data[y][x + 1][0] == '*' and ( not data[y][x + 1][1]):
    x, y = x + 1, y
    ans += 'R'
elif data[y + 1][x][0] == '*' and ( not data[y + 1][x][1]):
    x, y = x, y + 1
    ans += 'D'
while True:
    x, y = next1(x, y)
    if x == None and y == None:
        break
    else:
        x1, y1 = x, y
if x1 - startx == 1:
    ans += 'L'
elif x1 - startx == -1:
    ans += 'R'
elif y1 - starty == 1:
    ans += 'U'
elif y1 - starty == -1:
    ans += 'D'
print(ans)
