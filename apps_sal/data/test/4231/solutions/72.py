rows, columns = list(map(int, input().split()))
black_rows, black_columns = list(map(int, input().split()))

area = rows * columns
black_space = black_columns * rows + black_rows * columns - black_rows * black_columns

print((area - black_space))

