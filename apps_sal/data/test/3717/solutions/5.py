n = int(input())
u = []
for i in range(n):
    u.append(list(map(int, input().split())))
(l1, l2) = (max(u[0][0], u[1][0]), min(u[0][0], u[1][0]))
(d1, d2) = (max(u[0][1], u[1][1]), min(u[0][1], u[1][1]))
(r1, r2) = (min(u[0][2], u[1][2]), max(u[0][2], u[1][2]))
(u1, u2) = (min(u[0][3], u[1][3]), max(u[0][3], u[1][3]))
for i in range(2, n):
    if u[i][0] > l1:
        (l1, l2) = (u[i][0], l1)
    elif u[i][0] > l2:
        l2 = u[i][0]
    if u[i][1] > d1:
        (d1, d2) = (u[i][1], d1)
    elif u[i][1] > d2:
        d2 = u[i][1]
    if u[i][2] < r1:
        (r1, r2) = (u[i][2], r1)
    elif u[i][2] < r2:
        r2 = u[i][2]
    if u[i][3] < u1:
        (u1, u2) = (u[i][3], u1)
    elif u[i][3] < u2:
        u2 = u[i][3]
for i in range(n):
    if u[i][0] == l1:
        u[i][0] = l2
    else:
        u[i][0] = l1
    if u[i][1] == d1:
        u[i][1] = d2
    else:
        u[i][1] = d1
    if u[i][2] == r1:
        u[i][2] = r2
    else:
        u[i][2] = r1
    if u[i][3] == u1:
        u[i][3] = u2
    else:
        u[i][3] = u1
    if u[i][0] <= u[i][2] and u[i][1] <= u[i][3]:
        print(u[i][0], u[i][1])
        break
