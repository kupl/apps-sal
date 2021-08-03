t = int(input())

for _ in range(t):
    n, m = [int(x) for x in input().split()]
    grid = [[int(x) for x in input().split()] for _ in range(n)]

    rows = sum(1 for x in grid if all(y == 0 for y in x))
    cols = sum(1 for j in range(m) if all(grid[i][j] == 0 for i in range(n)))

    res = min(rows, cols)

    print("Ashish" if res % 2 else "Vivek")
