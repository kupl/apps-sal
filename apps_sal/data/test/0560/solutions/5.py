(r, c) = list(map(int, input().split()))
str = []
for i in range(0, r):
    aLine = input()
    str.append(aLine)
res = 0
for i in range(0, r):
    k = 1
    for j in range(0, c):
        if str[i][j] == 'S':
            k = 0
            break
    if k == 1:
        res = res + c
        str[i] = ''
        for j in range(0, c):
            str[i] = str[i] + '0'
for j in range(0, c):
    k = 1
    for i in range(0, r):
        if str[i][j] == 'S':
            k = 0
            break
    if k == 1:
        for i in range(0, r):
            if str[i][j] == '.':
                res = res + 1
print(res)
