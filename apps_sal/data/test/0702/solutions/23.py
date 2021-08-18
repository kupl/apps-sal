n = int(input())
field = [list(input()) for i in range(n)]
ans = 1
for i in range(n):
    for j in range(n):
        if field[i][j] == ".":
            if i > n - 3 or j == n - 1 or field[i + 1][j] != "." or field[i + 2][j] != "." or field[i + 1][j + 1] != "." or field[i + 1][j - 1] != ".":
                ans = 0
                break
            field[i + 1][j] = "
            field[i + 2][j] = "
            field[i + 1][j + 1] = "
            field[i + 1][j - 1] = "
    if ans == 0:
        break
if ans == 1:
    print("YES")
else:
    print("NO")
