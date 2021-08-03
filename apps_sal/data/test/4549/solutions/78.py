H, W = map(int, input().split())
x = [list(map(str, list(input()))) for l in range(H)]

for i in range(len(x)):
    x[i].insert(0, ".")
    x[i].append(".")
x.insert(0, ["."] * (W + 2))
x.append(["."] * (W + 2))

for i in range(1, H + 1):
    for j in range(1, W + 1):
        if x[i][j] == "#":
            if x[i][j - 1] == x[i][j + 1] == x[i - 1][j] == x[i + 1][j] == ".":
                print("No")
                return
print("Yes")
