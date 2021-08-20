c = [list(map(int, input().split())) for _ in range(3)]
ans = 'Yes'
for i in range(2):
    if c[i + 1][1] - c[i + 1][0] != c[0][1] - c[0][0]:
        ans = 'No'
    if c[i + 1][2] - c[i + 1][1] != c[0][2] - c[0][1]:
        ans = 'No'
for j in range(2):
    if c[1][i + 1] - c[0][i + 1] != c[1][0] - c[0][0]:
        ans = 'No'
    if c[2][i + 1] - c[1][i + 1] != c[2][0] - c[1][0]:
        ans = 'No'
print(ans)
