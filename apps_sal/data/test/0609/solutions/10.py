n = int(input())
field = [input().strip() for x in range(n)]
for i in range(n):
    for j in range(n):
        if (j == i and field[i][j] != field[0][0]) or (j == n - 1 - i and field[i][j] != field[0][0]) or (n > 2) * (j not in [i, n - i - 1] and (field[i][j] != field[0][1] or field[i][j] == field[0][0])):
            print('NO')
            return
print('YES')

