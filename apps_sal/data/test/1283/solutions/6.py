n, k = [int(i) for i in input().split(' ')]
grid = [input() for i in range(n)]

grid_score = [[0 for i in range(n)] for j in range(n)]

for row in range(n):
    for col in range(n - k + 1):
        if all(['.' == grid[row][col + x] for x in range(k)]):
            for x in range(k):
                grid_score[row][col + x] += 1

for row in range(n - k + 1):
    for col in range(n):
        if all(['.' == grid[row + x][col] for x in range(k)]):
            for x in range(k):
                grid_score[row + x][col] += 1

max_score = 0
max_row = 0
max_col = 0
for row in range(n):
    for col in range(n):
        if grid_score[row][col] > max_score:
            max_score = grid_score[row][col]
            max_row = row
            max_col = col

print(max_row + 1, max_col + 1)

