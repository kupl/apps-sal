n, k = map(int, input().split())

c_p1 = [[-1] * 2001 for x in range(2001)]
c_p2 = [[-1] * 2001 for x in range(2001)]

r_p1 = [[-1] * 2001 for x in range(2001)]
r_p2 = [[-1] * 2001 for x in range(2001)]

cells = []
for i in range(n):

    cells.append(input())

bonus = 0

for y in range(n):
    earliest = -1
    latest = -1
    for x in range(n):
        if cells[y][x] == "B":
            earliest = x
            break
    for x in range(n):
        if cells[y][n - x - 1] == "B":
            latest = n - x - 1
            break

    if earliest == -1:
        bonus += 1
    for x in range(n - k + 1):
        r_p1[y][x] = int(earliest >= x and x + k - 1 >= latest)

for x in range(n - k + 1):
    sum = 0
    for y in range(n):
        sum += r_p1[y][x]
        if y - k >= 0:
            sum -= r_p1[y - k][x]

        if y - k + 1 >= 0:
            r_p2[y - k + 1][x] = sum


for x in range(n):
    earliest = -1
    latest = -1
    for y in range(n):
        if cells[y][x] == "B":
            earliest = y
            break
    for y in range(n):
        if cells[n - y - 1][x] == "B":
            latest = n - y - 1
            break
    if earliest == -1:
        bonus += 1
    for y in range(n - k + 1):
        c_p1[y][x] = int(earliest >= y and y + k - 1 >= latest)

for y in range(n - k + 1):
    sum = 0
    for x in range(n):
        sum += c_p1[y][x]
        if x - k >= 0:
            sum -= c_p1[y][x - k]

        if x - k + 1 >= 0:
            c_p2[y][x - k + 1] = sum

ans = 0
for y in range(n - k + 1):
    for x in range(n - k + 1):
        ans = max(ans, c_p2[y][x] + r_p2[y][x])

print(ans + bonus)
