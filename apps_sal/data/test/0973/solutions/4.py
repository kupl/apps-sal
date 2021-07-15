r, c = list(map(int, input().split()))
cells = [list(input()) for _ in range(r)]

ans = "Yes"
for i in range(r):
    for j in range(c):
        if cells[i][j] == '.':
            cells[i][j] = 'D'
for i in range(r - 1):
    for j in range(c):
        if cells[i][j] == 'S' and cells[i + 1][j] == 'W':
            ans = "No"
        if cells[i][j] == 'W' and cells[i + 1][j] == 'S':
            ans = "No"
for i in range(r):
    for j in range(c - 1):
        if cells[i][j] == 'S' and cells[i][j + 1] == 'W':
            ans = "No"
        if cells[i][j] == 'W' and cells[i][j + 1] == 'S':
            ans = "No"
print(ans)
if ans == "Yes":
    for i in range(r):
        print(''.join(cells[i]))

