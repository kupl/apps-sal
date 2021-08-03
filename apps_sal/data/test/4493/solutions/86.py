c = [list(map(int, input().split())) for i in range(3)]
ans = "Yes"
for i in range(3):
    for j in range(3):
        if c[i][j] == c[i - 1][j] + c[i][j - 1] - c[i - 1][j - 1]:
            continue
        ans = "No"
print(ans)
