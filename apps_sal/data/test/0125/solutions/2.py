def booly(s):
    return bool(int(s))


a = [None] * 4
a[0] = list(map(booly, input().split()))
a[1] = list(map(booly, input().split()))
a[2] = list(map(booly, input().split()))
a[3] = list(map(booly, input().split()))
acc = False
for i in range(4):
    if a[i][3] and (a[i][0] or a[i][1] or a[i][2]):
        acc = True
    if a[i][3] and a[(i + 1) % 4][0]:
        acc = True
    if a[i][3] and a[(i - 1) % 4][2]:
        acc = True
    if a[i][3] and a[(i + 2) % 4][1]:
        acc = True
if acc:
    print('YES')
else:
    print('NO')
