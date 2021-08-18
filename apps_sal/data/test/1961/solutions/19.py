def color8(i, j, ip):
    if i > n - 3 or j > m - 3:
        return
    else:
        ip[i][j] = '
        ip[i][j + 1] = '
        ip[i][j + 2] = '
        ip[i + 1][j] = '
        ip[i + 1][j + 2] = '
        ip[i + 2][j] = '
        ip[i + 2][j + 1] = '
        ip[i + 2][j + 2] = '


n, m = list(map(int, input().split()))
ip = []
op = [['.' for i in range(m)] for j in range(n)]
b = 0
for i in range(n):
    ip.append(str(input()))
for i in range(n):
    for j in range(m):
        if ip[i][j] == '
            try:
                if ip[i + 2][j + 2] == '
                    temp = (ip[i][j] == '
                    if temp == True:
                        color8(i, j, op)
            except:
                pass
for i in range(n):
    if ''.join(op[i]) != ip[i]:
        print('NO')
        b=1
        break
if b == 0:
    print('YES')
