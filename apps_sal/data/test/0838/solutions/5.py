def sol():
    rows, cols = map(int, input().split())
    tab = [list(map(int, input().split())) for _ in range(rows)]
    res = rows * cols
    for row in range(rows):
        white = 0
        black = 0
        for col in range(cols):
            if tab[row][col] == 0:
                white += 1
            else:
                black += 1
        if white > 0:
            res += pow(2, white) - white - 1
        if black > 0:
            res += pow(2, black) - black - 1
    for col in range(cols):
        white = 0
        black = 0
        for row in range(rows):
            if tab[row][col] == 0:
                white += 1
            else:
                black += 1
        if white > 0:
            res += pow(2, white) - white - 1
        if black > 0:
            res += pow(2, black) - black - 1
    print(res)


sol()
