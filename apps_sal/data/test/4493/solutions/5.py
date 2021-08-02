c = []
for i in range(3):
    c.append(list(map(int, input().split())))

ans = True
for i in range(2):
    tmp = c[0][i + 1] - c[0][i]
    for j in range(2):
        if c[j + 1][i + 1] - c[j + 1][i] != tmp:
            ans = False
            break

for i in range(2):
    tmp = c[i + 1][0] - c[i][0]
    for j in range(2):
        if c[i + 1][j + 1] - c[i][j + 1] != tmp:
            ans = False
            break

if ans:
    print("Yes")
else:
    print("No")
