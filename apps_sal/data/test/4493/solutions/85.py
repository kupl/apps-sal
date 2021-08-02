c = [list(map(int, input().split())) for _ in range(3)]

flag = True

for i in range(1, 3):
    if not(c[i][0] - c[0][0] == c[i][1] - c[0][1] == c[i][2] - c[0][2]):
        flag = False
    if not(c[0][i] - c[0][0] == c[1][i] - c[1][0] == c[2][i] - c[2][0]):
        flag = False

if flag:
    print("Yes")
else:
    print("No")
