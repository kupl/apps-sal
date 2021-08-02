H, W = map(int, input().split())
a = [list(input()) for _ in range(H)]

# 行
r = [0] * H  # 行ごとの#の数
for i in range(H):
    r[i] = a[i].count('#')
# 列
c = [0] * W  # 列ごとの#の数
for i in a:
    for j in range(W):
        if i[j] == '#':
            c[j] += 1

for i in range(H):
    a[i] = [a[i][j] for j in range(W) if c[j] != 0]


for i in range(H):
    if r[i] != 0:
        print(''.join(a[i]))
