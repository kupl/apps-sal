c = [
    list(map(int, input().split()))
    for _ in range(3)
]

f = True
for j in range(2):
    x = c[j][0] - c[j + 1][0]
    y = c[0][j] - c[0][j + 1]
    for i in range(3):
        if c[j][i] - c[j + 1][i] != x:
            f = False
        if c[i][j] - c[i][j + 1] != y:
            f = False
print(['No', 'Yes'][int(f)])
