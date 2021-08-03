n, m = map(int, input().split())
grid = [input() for line in range(n)]
rows = len([line for line in grid if line == '.' * m])
cols = len([True for col in range(m) if len([row[col] for row in grid if row[col] == '.']) == n])
print(rows * m + cols * n - rows * cols)
