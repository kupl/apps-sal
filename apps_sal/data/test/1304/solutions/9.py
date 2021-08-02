field = []
for i in range(3):
    for j in range(3):
        line = input().split()
        field.append(''.join(line))
    a = list(map(int, input().split()))

a, b = a[0], a[1]
c, d = a % 3 + (3 * (a % 3 == 0)), b % 3 + (3 * (b % 3 == 0))
#print(a, b, c, d)
isfree = 0
for i in range(3 * (c - 1), 3 * c):
    for j in range(3 * (d - 1), 3 * d):
        if field[i][j] == '.':
            isfree += 1

if not isfree:
    # print(isfree)
    for i in range(9):
        for j in range(9):
            if field[i][j] == '.':
                field[i] = field[i][:j] + '!' + field[i][j + 1:]
else:
    for i in range(3 * (c - 1), 3 * c):
        for j in range(3 * (d - 1), 3 * d):
            if field[i][j] == '.':
                field[i] = field[i][:j] + '!' + field[i][j + 1:]

for i in range(3):
    for j in range(3):
        print(field[3 * i + j][:3], field[3 * i + j][3:6], field[3 * i + j][6:9])
    print()
