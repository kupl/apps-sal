n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
l1, l2 = max(a[0][0], a[1][0]), min(a[0][0], a[1][0])
d1, d2 = max(a[0][1], a[1][1]), min(a[0][1], a[1][1])
r1, r2 = min(a[0][2], a[1][2]), max(a[0][2], a[1][2])
u1, u2 = min(a[0][3], a[1][3]), max(a[0][3], a[1][3])
for i in range(2, n):
    if a[i][0] > l1:
        l1, l2 = a[i][0], l1
    elif a[i][0] > l2:
        l2 = a[i][0]
    if a[i][1] > d1:
        d1, d2 = a[i][1], d1
    elif a[i][1] > d2:
        d2 = a[i][1]
    if a[i][2] < r1:
        r1, r2 = a[i][2], r1
    elif a[i][2] < r2:
        r2 = a[i][2]
    if a[i][3] < u1:
        u1, u2 = a[i][3], u1
    elif a[i][3] < u2:
        u2 = a[i][3]
for i in range(n):
    if a[i][0] == l1:
        a[i][0] = l2
    else:
        a[i][0] = l1
    if a[i][1] == d1:
        a[i][1] = d2
    else:
        a[i][1] = d1
    if a[i][2] == r1:
        a[i][2] = r2
    else:
        a[i][2] = r1
    if a[i][3] == u1:
        a[i][3] = u2
    else:
        a[i][3] = u1
    if a[i][0] <= a[i][2] and a[i][1] <= a[i][3]:
        print(a[i][0], a[i][1])
        return
