h, w = map(int, input().split())
c = [input() for _ in range(h)]

for i in range(h):
    for j in range(w):
        if c[i][j] == "
        upper = c[i - 1][j] == "
        lower = c[i + 1][j] == "
        left = c[i][j - 1] == "
        right = c[i][j + 1] == "

        if not (upper or lower or left or right):
            print("No")
            break
    else:
        continue
    break
else:
    print("Yes")
