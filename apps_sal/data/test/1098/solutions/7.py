n = int(input())
s = ['.'] * n
mx = 0
for i in range(n):
    s[i] = input()
if n == 1:
    print('23:59')
else:
    s = sorted(s)
    for i in range(n):
        i1 = i
        i2 = (i + 1) % n
        col1 = int(s[i1][0:2]) * 60 + int(s[i1][3:5])
        col2 = int(s[i2][0:2]) * 60 + int(s[i2][3:5])
        if col1 > col2:
            if mx < col2 + 60 * 24 - col1 - 1:
                mx = col2 + 60 * 24 - col1 - 1
        else:
            if mx < col2 - col1 - 1:
                mx = col2 - col1 - 1
    print((mx // 60) // 10, (mx // 60) % 10, ':', (mx % 60) // 10, (mx % 60) % 10, sep='')
