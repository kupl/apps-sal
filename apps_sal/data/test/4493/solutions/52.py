l = []
for i in range(3):
    c1, c2, c3 = map(int, input().split())
    l.append([c1, c2, c3])

b1 = l[0][0]
b2 = l[1][0]
b3 = l[2][0]

flag = 0
for i in range(3):
    if not (l[0][1] - b1 == l[1][1] - b2 == l[2][1] - b3):
        flag = 1
    if not (l[0][2] - b1 == l[1][2] - b2 == l[2][2] - b3):
        flag = 1
if flag == 1:
    print('No', flush=True)
else:
    print('Yes', flush=True)
