n, m = map(int, input().split())

grid = [None] * n

for i in range(n):
    grid[i] = list(map(int, input().split()))

result = 0

for i in range(n):
    t = sum(grid[i])
    result += 2**t + 2**(m - t)

for i in range(m):
    t = sum(grid[j][i] for j in range(n))
    result += 2**t + 2**(n - t)

result -= 2 * (n + m) + n * m

print(result)
