
l1 = input()
l2 = input()
l3 = input()
l4 = input()

grid = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

cross = 0
dots = []
for i in range(0, 4):
    if l1[i] == ".":
        dots += [[0 + 2, i + 2]]
    elif l1[i] == "x":
        cross += 1
        grid[0 + 2][i + 2] = 1

    if l2[i] == ".":
        dots += [[1 + 2, i + 2]]
    elif l2[i] == "x":
        cross += 1
        grid[1 + 2][i + 2] = 1

    if l3[i] == ".":
        dots += [[2 + 2, i + 2]]
    elif l3[i] == "x":
        cross += 1
        grid[2 + 2][i + 2] = 1

    if l4[i] == ".":
        dots += [[3 + 2, i + 2]]
    elif l4[i] == "x":
        cross += 1
        grid[3 + 2][i + 2] = 1


def check(dot, dir, delta):
    nonlocal grid
    grid[dot[0]][dot[1]] = 1

    acc = 1
    if dir == 0:  # horizontal
        for i in range(delta, delta + 3):
            acc *= grid[dot[0] + i][dot[1]]
    elif dir == 1:  # vertical
        for i in range(delta, delta + 3):
            acc *= grid[dot[0]][dot[1] + i]
    elif dir == 2:  # diag1
        for i in range(delta, delta + 3):
            acc *= grid[dot[0] + i][dot[1] + i]
    elif dir == 3:  # diag2
        for i in range(delta, delta + 3):
            acc *= grid[dot[0] + i][dot[1] - i]

    grid[dot[0]][dot[1]] = 0
    return acc


if cross < 2 or len(dots) == 0:
    print("NO")
else:
    for dot in dots:
        for dir in range(0, 4):
            for delta in range(-2, 1):
                if check(dot, dir, delta) == 1:
                    print("YES")
                    return
print("NO")
