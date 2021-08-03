n = int(input())
l = [[0] * 10 for i in range(10)]

for i in range(1, min(10, n + 1), 1):
    l[i][i] += 1

if len(str(n)) >= 2:
    for k in range(2, len(str(n)), 1):
        for i in range(1, 10, 1):
            for j in range(1, 10, 1):
                l[i][j] += 10**(k - 2)

    for i in range(1, int(str(n)[0]), 1):
        for j in range(1, 10, 1):
            l[i][j] += 10**(len(str(n)) - 2)
    if len(str(n)) >= 3:
        for j in range(1, 10, 1):
            if j <= int(str(n)[-1]):
                l[int(str(n)[0])][j] += int(str(n)[1:-1]) + 1
            else:
                l[int(str(n)[0])][j] += int(str(n)[1:-1])
    else:
        for j in range(1, 10, 1):
            if j <= int(str(n)[-1]):
                l[int(str(n)[0])][j] += 1

t = 0
for i in range(1, 10, 1):
    for j in range(1, 10, 1):
        t += l[i][j] * l[j][i]

print(t)
