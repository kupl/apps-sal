def main():
    (h, w, m) = map(int, input().split())
    row = [0] * (h + 1)
    col = [0] * (w + 1)
    d = set({})
    for _ in range(m):
        (a, b) = map(int, input().split())
        row[a] += 1
        col[b] += 1
        d.add((a, b))
    max_row = max(row)
    max_col = max(col)
    max_row_d = set({})
    max_col_d = set({})
    for i in range(1, h + 1):
        if row[i] == max_row:
            max_row_d.add(i)
    for i in range(1, w + 1):
        if col[i] == max_col:
            max_col_d.add(i)
    sm = max_row + max_col
    for i in max_row_d:
        for j in max_col_d:
            if (i, j) in d:
                continue
            break
        else:
            continue
        break
    else:
        sm -= 1
    print(sm)


main()
