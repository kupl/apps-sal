n, m = list(map(int, input().strip().split()))

remains = n*n
deleted_rows = set()
deleted_cols = set()
answer = []
for _ in range(m):
    c, r = list(map(int, input().strip().split()))
    col_deleted = c in deleted_cols
    row_deleted = r in deleted_rows
    if not (col_deleted and row_deleted):
        if col_deleted:
            remains -= (n - len(deleted_cols))
        elif row_deleted:
            remains -= (n - len(deleted_rows))
        else:  # not x_in and not y_in
            remains -= (2*n - len(deleted_cols) - len(deleted_rows) - 1)

    deleted_cols.add(c)
    deleted_rows.add(r)

    answer.append(str(remains))

print(' '.join(answer))

