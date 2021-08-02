lines = int(input())
grid = []
result = "YES"

for i in range(lines):
    grid.append(input())

x_char = grid[0][0]

test = ("".join([i for i in grid]))

if len("".join(set(test))) > 2:
    result = "NO"
else:
    for i in range(lines // 2 + 1):
        if grid[i] != grid[-(i + 1)]:
            result = "NO"
            break
        if grid[i][i] != grid[i][-(i + 1)]:
            result = "NO"
            break
        if grid[i][i] != x_char:
            result = "NO"
            break
        if grid[i].count(x_char) > 2:
            result = "NO"
            break
if grid[lines // 2].count(x_char) > 1:
    result = "NO"

print(result)
