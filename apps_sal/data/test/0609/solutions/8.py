n = int(input())
b = [input() for i in range(n)]
l = b[0][0]
c = b[0][1]
flag = True
for i in range(n):
    if i == n // 2:
        if b[i][i] != l or b[i].count(l) != 1 or b[i].count(c) != n - 1:
            flag = False
            break
    elif b[i][i] != l or b[i][n - 1 - i] != l or b[i].count(l) != 2 or (b[i].count(c) != n - 2):
        flag = False
        break
if flag:
    print('YES')
else:
    print('NO')
