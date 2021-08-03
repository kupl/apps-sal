def codeforces(piece):
    row_number = 0
    for row in piece:
        num = row.count('X')
        if num == 0:
            continue
        if row_number == 0:
            row_number = num
            continue
        if num != row_number:
            return 'NO'

    col_number = 0
    cols = [[row[i] for row in piece] for i in range(len(piece[0]))]
    for col in cols:
        num = col.count('X')
        if num == 0:
            continue
        if col_number == 0:
            col_number = num
            continue
        if num != col_number:
            return 'NO'

    return 'YES'


rows, _ = input().split()
rows = int(rows)
piece = []
for _ in range(rows):
    line = input()
    piece.append(line)

print(codeforces(piece))
