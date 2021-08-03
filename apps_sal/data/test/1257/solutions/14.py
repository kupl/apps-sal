sLine = input()
sSplit = sLine.split()
n = int(sSplit[0])
k = int(sSplit[1])
v = []
for i in range(n):
    v.append([])
    for j in range(n):
        v[i].append(0)
x1 = n * n
x2 = 1
for i in range(n):
    for j in range(n - 1, (k - 1) - 1, -1):
        v[i][j] = x1
        x1 -= 1
    for j in range(0, (k - 1), 1):
        v[i][j] = x2
        x2 += 1
nSum = 0
for i in range(n):
    nSum += v[i][k - 1]
print(nSum)
for i in range(n):
    for j in range(n):
        print(v[i][j], end='')
        if j == n - 1:
            print('')
        else:
            print(' ', end='')
