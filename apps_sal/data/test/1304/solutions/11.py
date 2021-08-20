k = []
for i in range(11):
    a = input()
    if i != 3 and i != 7:
        k.append(a[0] + a[1] + a[2] + a[4] + a[5] + a[6] + a[8] + a[9] + a[10] + ' ')
(a, b) = map(int, input().split())
a -= 1
b -= 1
x = a % 3
y = b % 3
r = 1
for i in range(3):
    s = k[x * 3 + i]
    for j in range(3):
        if s[y * 3 + j] == '.':
            s = s[:y * 3 + j] + '!' + s[y * 3 + j + 1:]
            r = 0
    k[x * 3 + i] = s
if r == 1:
    for i in range(9):
        s = k[i]
        for j in range(9):
            if s[j] == '.':
                s = s[:j] + '!' + s[j + 1:]
        k[i] = s
for i in range(9):
    for j in range(9):
        print(k[i][j], end='')
        if j == 2 or j == 5:
            print(' ', end='')
    print('')
    if i == 2 or i == 5:
        print('')
