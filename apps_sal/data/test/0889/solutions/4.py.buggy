import sys
a = [input(), input(), input(), input()]
for i in range(0, 3):
    for j in range(0, 3):
        if a[i:i + 2][0][j:j + 2].count('#') + a[i:i + 2][1][j:j + 2].count('#') > 2 or a[i:i + 2][0][j:j + 2].count('.') + a[i:i + 2][1][j:j + 2].count('.') > 2:
            print('YES')
            return
print('NO')
