n = int(input())

cubes = []
for i in range(n):
    cubes.append(list(map(int, input().split())))

numbers = set()

if n == 3:
    for i in range(6):
        numbers.add(cubes[0][i])
        numbers.add(cubes[1][i])
        numbers.add(cubes[2][i])
        for j in range(6):
            numbers.add(cubes[0][i] * 10 + cubes[1][j])
            numbers.add(cubes[0][i] * 10 + cubes[2][j])
            numbers.add(cubes[1][i] * 10 + cubes[0][j])
            numbers.add(cubes[1][i] * 10 + cubes[2][j])
            numbers.add(cubes[2][i] * 10 + cubes[0][j])
            numbers.add(cubes[2][i] * 10 + cubes[1][j])
            for k in range(6):
                numbers.add(cubes[0][i] * 100 + cubes[1][j] * 10 + cubes[2][k])
                numbers.add(cubes[0][i] * 100 + cubes[2][j] * 10 + cubes[1][k])
                numbers.add(cubes[1][i] * 100 + cubes[0][j] * 10 + cubes[2][k])
                numbers.add(cubes[1][i] * 100 + cubes[2][j] * 10 + cubes[0][k])
                numbers.add(cubes[2][i] * 100 + cubes[0][j] * 10 + cubes[1][k])
                numbers.add(cubes[2][i] * 100 + cubes[1][j] * 10 + cubes[0][k])
if n == 2:
    for i in range(6):
        numbers.add(cubes[0][i])
        numbers.add(cubes[1][i])
        for j in range(6):
            numbers.add(cubes[0][i] * 10 + cubes[1][j])
            numbers.add(cubes[1][i] * 10 + cubes[0][j])
if n == 1:
    for i in range(6):
        numbers.add(cubes[0][i])

ans = 0
for i in range(1, 999):
    if i not in numbers:
        break
    ans = i

print(ans)
