com = int(input())
zar = []
y = 0
for i in range(com):
    line = [int(x) for x in input().split(' ')]
    zar.append(line)

for i in range(com):
    l = 0
    for j in range(1, zar[i][0] + 1):
        if l < zar[i][j]:
            l = zar[i][j]
    zar[i][1] = l

for i in range(com - 1):
    u = 0
    if zar[0][1] > zar[i + 1][1]:
        u = zar[0][1] - zar[i + 1][1]
        y += u * zar[i + 1][0]
    else:
        u = zar[i + 1][1] - zar[0][1]
        y += u * zar[0][0]
        zar[0][1] = zar[i + 1][1]
    zar[0][0] += zar[i + 1][0]
print(y)
