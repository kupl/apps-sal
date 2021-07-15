n = int(input())
aij = [list(map(str,input().split())) for i in range(n)]
numbers = [0]*1001
numbers[0] = 1
for i in range(n):
    for j in range(6):
        numbers[int(aij[i][j])] = 1
if n == 2:
    for i in range(6):
        for j in range(6):
            numbers[int(aij[0][i]+aij[1][j])] = 1
            numbers[int(aij[1][j]+aij[0][i])] = 1
if n == 3:
        for i in range(6):
            for j in range(6):
                numbers[int(aij[0][i]+aij[1][j])] = 1
                numbers[int(aij[1][j]+aij[0][i])] = 1
        for i in range(6):
            for j in range(6):
                numbers[int(aij[1][i]+aij[2][j])] = 1
                numbers[int(aij[2][j]+aij[1][i])] = 1
        for i in range(6):
            for j in range(6):
                numbers[int(aij[0][i]+aij[2][j])] = 1
                numbers[int(aij[2][j]+aij[0][i])] = 1
        for i in range(6):
            for j in range(6):
                for z in range(6):
                    numbers[int(aij[0][i]+aij[1][j]+aij[2][z])] = 1
                    numbers[int(aij[0][i]+aij[2][z]+aij[1][j])] = 1
                    numbers[int(aij[1][j]+aij[0][i]+aij[2][z])] = 1
                    numbers[int(aij[1][j]+aij[2][z]+aij[0][i])] = 1
                    numbers[int(aij[2][z]+aij[1][j]+aij[0][i])] = 1
                    numbers[int(aij[2][z]+aij[0][i]+aij[1][j])] = 1
ans = -1
for i in range(1001):
    if numbers[i] == 0:
        break
    ans += 1
print(ans)

