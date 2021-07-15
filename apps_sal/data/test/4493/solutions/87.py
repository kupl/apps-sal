
c = [list(map(int, input().split())) for i in range(3)]

flag = False
for a0 in range(-100, 200):
    b0 = c[0][0] - a0
    a1 = c[1][0] - b0
    a2 = c[2][0] - b0
    b1 = c[0][1] - a0
    b2 = c[0][2] - a0
    if (a1 + b1 == c[1][1]
            and a2 + b1 == c[2][1]
            and a1 + b2 == c[1][2]
            and a2 + b2 == c[2][2]):
        flag = True

if flag:
    print("Yes")
else:
    print("No")
