a = list(map(str, input()))
b = list(map(str, input()))

if a[0] == b[2] and a[1] == b[1] and a[2] == b[0]:
    print('YES')
else:
    print('NO')
