def change(n):
    if n == 0:
        n = 1
    else:
        n = 0
    return n


table = []
for i in range(3):
    table.append(list(map(int, input().split())))
row = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
for i in range(3):
    for j in range(3):
        if table[i][j] % 2 == 0:
            continue
        else:
            row[i][j] = change(row[i][j])
            if i == 0:
                if j == 0:
                    row[i][j + 1] = change(row[i][j + 1])
                    row[i + 1][j] = change(row[i + 1][j])
                elif j == 1:
                    row[i][j + 1] = change(row[i][j + 1])
                    row[i][j - 1] = change(row[i][j - 1])
                    row[i + 1][j] = change(row[i + 1][j])
                elif j == 2:
                    row[i][j - 1] = change(row[i][j - 1])
                    row[i + 1][j] = change(row[i + 1][j])
            elif i == 1:
                if j == 0:
                    row[i][j + 1] = change(row[i][j + 1])
                    row[i - 1][j] = change(row[i - 1][j])
                    row[i + 1][j] = change(row[i + 1][j])
                elif j == 1:
                    row[i][j + 1] = change(row[i][j + 1])
                    row[i][j - 1] = change(row[i][j - 1])
                    row[i + 1][j] = change(row[i + 1][j])
                    row[i - 1][j] = change(row[i - 1][j])
                elif j == 2:
                    row[i][j - 1] = change(row[i][j - 1])
                    row[i + 1][j] = change(row[i + 1][j])
                    row[i - 1][j] = change(row[i - 1][j])
            elif i == 2:
                if j == 0:
                    row[i][j + 1] = change(row[i][j + 1])
                    row[i - 1][j] = change(row[i - 1][j])
                elif j == 1:
                    row[i][j + 1] = change(row[i][j + 1])
                    row[i][j - 1] = change(row[i][j - 1])
                    row[i - 1][j] = change(row[i - 1][j])
                elif j == 2:
                    row[i - 1][j] = change(row[i - 1][j])
                    row[i][j - 1] = change(row[i][j - 1])
for i in range(3):
    rowo = ''
    for j in range(3):
        rowo += str(row[i][j])
    print(rowo)
