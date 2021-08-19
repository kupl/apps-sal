a = []
for _ in range(4):
    a.append(list(map(lambda x: int(x == '#'), input())))
res = False
for i in range(3):
    for j in range(3):
        res = res or (a[i][j] + a[i + 1][j] + a[i][j + 1] + a[i + 1][j + 1] != 2)
print('YES' if res else 'NO')
