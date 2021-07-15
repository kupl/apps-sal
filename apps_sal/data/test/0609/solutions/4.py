n = int(input().strip())
a = []
for i in range(n):
    a.append(input().strip())
ch = a[0][0]
fl = True
for i in range(n):
    if a[i][i] != ch or a[i][n - i - 1] != ch:
        fl = False
        break
ch2 = a[0][1]
if ch == ch2:
    fl = False
for i in range(n):
    for j in range(n):
        if i != j and j != n - i - 1:
            if a[i][j] != ch2:
                fl = False
                break
            
if fl:
    print('YES')
else:
    print('NO')
