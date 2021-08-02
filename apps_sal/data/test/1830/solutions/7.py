import sys

n, rooks = map(int, input().split())

rows = [False for _ in range(n + 1)]
columns = [False for _ in range(n + 1)]

empty_rows = n
empty_columns = n

for i in range(rooks):
    x, y = map(int, input().split())
    if not rows[x]:
        rows[x] = True
        empty_rows -= 1
    if not columns[y]:
        columns[y] = True
        empty_columns -= 1
    if i == rooks - 1:
        print(empty_rows * empty_columns)
    else:
        print(empty_rows * empty_columns, end=' ')
