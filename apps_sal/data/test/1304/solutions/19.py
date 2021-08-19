a = []
for i in range(0, 3):
    a.append(input().split())
s = input()
for i in range(0, 3):
    a.append(input().split())
d = input()
for i in range(0, 3):
    a.append(input().split())
(q, w) = list(map(int, input().split()))
z = q % 3 - 1
if z == -1:
    z = 2
x = w % 3 - 1
if x == -1:
    x = 2
z = z * 3
b = True
for i in range(z, z + 3):
    if a[i][x].count('.') != 0:
        b = False
        a[i][x] = a[i][x].replace('.', '!')
if b:
    for i in range(0, 9):
        for j in range(0, 3):
            a[i][j] = a[i][j].replace('.', '!')
for i in range(0, 3):
    print(' '.join(a[i]))
print()
for i in range(3, 6):
    print(' '.join(a[i]))
print()
for i in range(6, 9):
    print(' '.join(a[i]))
