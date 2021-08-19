x = [0 for i in range(3)]
y = [0 for i in range(3)]
mark = [False, False, False]
mark1 = [False, False, False]
for i in range(3):
    (x[i], y[i]) = list(map(int, input().split()))
xp = []
yp = []
for i in range(3):
    for j in range(i + 1, 3):
        if x[i] == x[j]:
            xp.append([i, j])
            mark[i] = True
            mark[j] = True
        if y[j] == y[i]:
            yp.append([i, j])
            mark1[i] = True
            mark1[j] = True
if len(xp) == 3 or len(yp) == 3:
    print(1)
elif len(xp) == 1:
    if not mark[0]:
        if y[0] >= max(y[1], y[2]) or y[0] <= min(y[1], y[2]):
            print(2)
        else:
            print(3)
    elif not mark[1]:
        if y[1] >= max(y[0], y[2]) or y[1] <= min(y[0], y[2]):
            print(2)
        else:
            print(3)
    if not mark[2]:
        if y[2] >= max(y[1], y[0]) or y[2] <= min(y[1], y[0]):
            print(2)
        else:
            print(3)
elif len(yp) == 1:
    if not mark1[0]:
        if x[0] >= max(x[1], x[2]) or x[0] <= min(x[1], x[2]):
            print(2)
        else:
            print(3)
    elif not mark1[1]:
        if x[1] >= max(x[0], x[2]) or x[1] <= min(x[0], x[2]):
            print(2)
        else:
            print(3)
    if not mark1[2]:
        if x[2] >= max(x[1], x[0]) or x[2] <= min(x[1], x[0]):
            print(2)
        else:
            print(3)
else:
    print(3)
