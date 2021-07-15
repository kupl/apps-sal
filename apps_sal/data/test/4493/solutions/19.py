c = [list(map(int, input().split())) for _ in range(3)]

for i in range(1, 3):
    d = c[i][0] - c[0][0]
    e = c[0][i] - c[0][0]
    for j in range(1, 3):
        if d != c[i][j] - c[0][j]:
            print("No")
            return
        if e != c[j][i] - c[j][0]:
            print("No")
            return
print("Yes")
