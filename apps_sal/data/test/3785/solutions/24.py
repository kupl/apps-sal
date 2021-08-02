n, m, k = list(map(int, input().split()))
maze = [["#"] * (m + 2)] + [list("#" + input() + "#") for i in range(n)] + [["#"] * (m + 2)]
steps = [[0, 1], [0, -1], [1, 0], [-1, 0]]

empty = -k
x, y = None, None
for i in range(n + 2):
    empty += maze[i].count(".")
    for j in range(m + 2):
        if maze[i][j] == ".":
            x, y = i, j
            break

stack = [(x, y)]
while empty:
    (x, y) = stack.pop()
    if maze[x][y] == "v":
        continue
    for dx, dy in steps:
        if maze[x + dx][y + dy] == ".":
            stack.append((x + dx, y + dy))
    maze[x][y] = "v"
    empty -= 1

for row in maze[1:-1]:
    print("".join(row[1:-1]).replace(".", "X").replace("v", "."))
