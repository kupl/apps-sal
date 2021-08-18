a = []
for i in range(4):
    a += [input().replace('
d=False
for i in range(9):
    b, c=i // 3, i % 3
    if sum(map(int, [a[b][c], a[b + 1][c], a[b][c + 1], a[b + 1][c + 1]])) != 2:
        d=True
        break
print('YES'if d else'NO')
