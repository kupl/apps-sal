n = int(input())
grid = [input() for _ in range(n)]
total = 0
if n <= 2:
    print(total)
    return
for r in range(1, n - 1):
    for c in range(1, n - 1):
        if grid[r][c] != 'X':
            continue
        if grid[r - 1][c - 1] == grid[r - 1][c + 1] == grid[r + 1][c - 1] == grid[r + 1][c + 1] == "X":
            total += 1
print(total)
