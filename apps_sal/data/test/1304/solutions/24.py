k = [[] for i in range(9)]
p = 0
r = 0
for i in range(11):
    b = input()
    b = b[:3] + b[4:7] + b[8:11]
    if b != '':
        k[i - p].append(b)
    else:
        p += 1
a, b = map(int, input().split())
a -= 1
b -= 1
for i in range(3 * (a % 3), 3 * (a % 3) + 3):
    for j in range(3 * (b % 3), 3 * (b % 3) + 3):
        if k[i][0][j] != 'o' and k[i][0][j] != 'x':
            k[i][0] = k[i][0][:j] + '!' + k[i][0][j + 1:]
            r = 1
if r == 0:
    for i in range(9):
        for j in range(9):
            if k[i][0][j] != 'o' and k[i][0][j] != 'x':
                k[i][0] = k[i][0][:j] + '!' + k[i][0][j + 1:]
for i in range(len(k)):
    for j in range(len(k[i][0])):
        print(k[i][0][j], end='')
        if j == 2 or j == 5:
            print(' ', end='')
    print(' ')
    if i == 2 or i == 5:
        print(' ')
