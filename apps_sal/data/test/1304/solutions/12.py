mass = []
for i in range(11):
    a = list(input())
    if i != 3 and i != 7:
        a.pop(3)
        a.pop(6)
        mass.append(a)
(x, y) = map(int, input().split())
x -= 1
y -= 1
n = 0
for i in range(x % 3 * 3, x % 3 * 3 + 3):
    for j in range(y % 3 * 3, y % 3 * 3 + 3):
        if mass[i][j] == '.':
            mass[i][j] = '!'
            n += 1
if n == 0:
    for i in range(9):
        for j in range(9):
            if mass[i][j] == '.':
                mass[i][j] = '!'
for i in range(9):
    mass[i].insert(3, ' ')
    mass[i].insert(7, ' ')
    if i == 3 or i == 6:
        print()
    for j in range(11):
        print(mass[i][j], end='')
    print()
