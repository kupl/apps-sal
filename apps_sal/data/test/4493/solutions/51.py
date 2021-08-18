c = [list(map(int, input().split())) for _ in range(3)]

ans = "Yes"
for i in range(2):
    if c[0][i] - c[0][i + 1] != c[1][i] - c[1][i + 1]:
        ans = "No"
    elif c[1][i] - c[1][i + 1] != c[2][i] - c[2][i + 1]:
        ans = "No"
    elif c[i][0] - c[i + 1][0] != c[i][1] - c[i + 1][1]:
        ans = "No"
    elif c[i][1] - c[i + 1][1] != c[i][2] - c[i + 1][2]:
        ans = "No"
print(ans)
