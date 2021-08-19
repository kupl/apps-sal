
S = [len(x) for x in input().split('T')]

x, y = map(int, input().split(" "))
xstart = 0
dir = 0  # 0→ x方向 1 →y方向
first = True

temp = 0
spin_count = 0
x_array = []
y_array = []

xstart = S[0]
for c in S[1:]:
    if c != 0:
        dir += 1
        dir %= 2
        temp = c
        if dir == 0:
            x_array.append(temp)
        else:
            y_array.append(temp)
    else:
        dir += 1


dpx = {}
dpx[xstart] = 1


for i in x_array:
    temp = []
    remove = []
    for k, v in dpx.items():
        if v != -1:
            temp.append(k + i)
            temp.append(k - i)
            remove.append(k)
    for k in remove:
        dpx[k] = -1
    for k in temp:
        dpx[k] = 1

dpy = {}
dpy[0] = 1
for i in y_array:
    temp = []
    remove = []

    for k, v in dpy.items():
        if v != -1:
            temp.append(k + i)
            temp.append(k - i)
            remove.append(k)
    for k in remove:
        dpy[k] = -1
    for k in temp:
        dpy[k] = 1

if x in dpx and y in dpy and dpx[x] == 1 and dpy[y] == 1:
    print("Yes")
else:
    print("No")
