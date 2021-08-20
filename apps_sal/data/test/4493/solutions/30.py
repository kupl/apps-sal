c = [list(map(int, input().split())) for _ in range(3)]
a = [0] * 3
b = [0] * 3
ok = True
b = c[0]
a[1] = c[1][0] - b[0]
a[2] = c[2][0] - b[0]
for i in range(3):
    for j in range(3):
        if c[i][j] != a[i] + b[j]:
            ok = False
if ok:
    print('Yes')
else:
    print('No')
