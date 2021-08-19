c = [''] * 2
c[0] = input()
c[1] = input()
s = True
for i in range(2):
    for j in range(3):
        if c[i][j] != c[-i - 1][-j - 1]:
            s = False
if s:
    print('YES')
else:
    print('NO')
