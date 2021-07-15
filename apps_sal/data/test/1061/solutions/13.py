for i in range(5):
    line = input().split()
    for j, value in enumerate(line):
        if value == "1":
            x, y = i, j

print(abs(x - 2) + abs(y - 2))

