n = int(input())
grid = []
for i in range(n):
    l1 = list(map(int, input().split()))
    grid.append(l1)
first = grid[0][1] * grid[0][2]
first = first // grid[1][2]
first = int(first**0.5)
result = [first]
for i in range(1, n):
    result.append(grid[0][i] // first)
print(*result, sep=" ")
