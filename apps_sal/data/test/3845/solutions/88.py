a, b = map(int, input().split())
n = 100

grid = [["#"] * n for _ in range(n // 2)] + [["."] * n for _ in range(n // 2)]

k = 0
cnt = 0
for i in range(a - 1):
    grid[k][2 * i - cnt] = "."
    if (2 * i) % 100 == n - 2:
        k += 2
        cnt += n

k = n // 2 + 1
cnt = 0
for i in range(b - 1):
    grid[k][2 * i - cnt] = "#"
    if (2 * i) % 100 == n - 2:
        k += 2
        cnt += n
print(100, 100)
for i in grid:
    print("".join(i))
