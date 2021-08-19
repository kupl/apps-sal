def LIHW(h):
    return [list(map(int, input().split())) for _ in range(h)]


masu = LIHW(3)
ans = 'Yes'
for i in range(2):
    if masu[i + 1][1] - masu[i + 1][0] != masu[0][1] - masu[0][0]:
        ans = 'No'
    if masu[i + 1][2] - masu[i + 1][1] != masu[0][2] - masu[0][1]:
        ans = 'No'
for i in range(2):
    if masu[1][i + 1] - masu[0][i + 1] != masu[1][0] - masu[0][0]:
        ans = 'No'
    if masu[2][i + 1] - masu[1][i + 1] != masu[2][0] - masu[1][0]:
        ans = 'No'
print(ans)
