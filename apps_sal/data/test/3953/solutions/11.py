n = int(input())
s = [''] * n
for i in range(n):
    s[i] = input()
row, col = 0, 0
for i in range(n):
    for j in range(n):
        if s[i][j] == '.':
            break
    else:
        row = 1
        break
for i in range(n):
    for j in range(n):
        if s[j][i] == '.':
            break
    else:
        col = 1
        break
if row == col == 1:
    print(-1)
    return
if row == 0:
    for i in range(n):
        for j in range(n):
            if s[i][j] == '.':
                print(i+1, j+1)
                break
else:
    for i in range(n):
        for j in range(n):
            if s[j][i] == '.':
                print(j+1, i+1)
                break

