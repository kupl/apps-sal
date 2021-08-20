n = int(input())
d = [0] * 110
d[0] = 1
for i in range(1, 105):
    if i - 3 >= 0:
        d[i] |= d[i - 3]
    if i - 7 >= 0:
        d[i] |= d[i - 7]
for i in range(n):
    m = int(input())
    if d[m]:
        print('YES')
    else:
        print('NO')
