c = []
for i in range(3):
    c.append(list(map(int, input().split())))
flag = True
for i in range(2):
    if flag == True and c[i][1] - c[i][0] == c[i + 1][1] - c[i + 1][0] and c[i][2] - c[i][1] == c[i + 1][2] - c[i + 1][1] and c[1][i] - c[0][i] == c[1][i + 1] - c[0][i + 1] and c[2][i] - c[1][i] == c[2][i + 1] - c[1][i + 1]:
        flag = True
    else:
        flag = False
if flag == True:
    print('Yes')
else:
    print('No')
