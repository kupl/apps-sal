from math import ceil
table = []
for i in range(3):
    var = []
    for _ in range(3):
        var.append(input().split())
    table.append(var)
    if i != 2:
        input()
(y, x) = [int(x) for x in input().split()]
x1 = x % 3 - 1
y1 = y % 3 - 1
for i in range(3):
    if '.' in table[y1][i][x1]:
        for j in range(3):
            table[y1][j][x1] = table[y1][j][x1].replace('.', '!')
        break
else:
    for i in range(3):
        for j in range(3):
            for k in range(3):
                table[i][j][k] = table[i][j][k].replace('.', '!')
for x in table:
    for y in x:
        print(*y)
    print()
