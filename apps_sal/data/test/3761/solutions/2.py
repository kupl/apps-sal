s = input()
x, y = list(map(int, input().split()))

flg = 1
x_list = []
y_list = []
tmp = 0
for i, si in enumerate(s):
    if si == 'F':
        tmp += 1
    else:
        if flg == 1:
            x_list.append(tmp)
        else:
            y_list.append(tmp)
        flg *= -1
        tmp = 0
if flg == 1:
    x_list.append(tmp)
else:
    y_list.append(tmp)

x = sum(x_list) - x
y = sum(y_list) - y
if x % 2 != 0 or y % 2 != 0:
    print('No')
    return

if x < 0 or y < 0:
    print('No')
    return

x //= 2
y //= 2

if s[0] == 'F':
    x_list.reverse()
    x_list.pop()

dpx = [[0] * (x + 1) for _ in range(len(x_list) + 1)]
dpx[0][0] = 1
dpy = [[0] * (y + 1) for _ in range(len(y_list) + 1)]
dpy[0][0] = 1
for i in range(len(x_list)):
    for j in range(x + 1):
        if dpx[i][j]:
            dpx[i + 1][j] = 1
            if j + x_list[i] <= x:
                dpx[i + 1][j + x_list[i]] = 1
for i in range(len(y_list)):
    for j in range(y + 1):
        if dpy[i][j]:
            dpy[i + 1][j] = 1
            if j + y_list[i] <= y:
                dpy[i + 1][j + y_list[i]] = 1

if dpx[-1][-1] and dpy[-1][-1]:
    print('Yes')
else:
    print('No')
