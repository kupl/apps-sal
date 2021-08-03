
for _ in range(int(input())):
    m, n = list(map(int, input().strip().split(' ')))
    grid = []
    for i in range(m):
        grid += [input()]
    row = []
    col = []
    MIN_row = 10**10
    MIN_col = 10**10
    for i in range(m):
        count = 0
        for j in range(n):
            if grid[i][j] == ".":
                count += 1
        row += [count]
        MIN_row = min(MIN_row, count)
    for j in range(n):
        count = 0
        for i in range(m):
            if grid[i][j] == ".":
                count += 1
        col += [count]
        MIN_col = min(MIN_col, count)

    want_row = set([])
    for i in range(len(row)):
        if row[i] == MIN_row:
            want_row.add(i)

    want_col = set([])
    for i in range(len(col)):
        if col[i] == MIN_col:
            want_col.add(i)

    flag = 0
    for i in range(len(row)):
        if flag == 1:
            break
        for j in range(len(col)):
            if grid[i][j] == ".":
                if i in want_row and j in want_col:
                    flag = 1
                    break

    print(MIN_row + MIN_col - flag)
