A, B = list(map(int, input().split()))
grid = []
for i in range(50):
    grid.append(["."] * (100))
for i in range(50):
    grid.append(["#"] * (100))

A -= 1
B -= 1

for i in range(0, 50, 2):
    for j in range(0, 100, 2):
        if B == 0:
            break
        grid[i][j] = "#"
        B -= 1
    else:
        continue
    break

grid = grid[::-1]
for i in range(0, 50, 2):
    for j in range(0, 100, 2):
        if A == 0:
            break
        grid[i][j] = "."
        A -= 1
    else:
        continue
    break

print("100 100")
for row in grid:
    print(("".join(row)))
