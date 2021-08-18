H, W = map(int, input().split())
a = [list(input()) for _ in range(H)]

r = [0] * H
for i in range(H):
    r[i] = a[i].count('
c=[0] * W
for i in a:
    for j in range(W):
        if i[j] == '
            c[j] += 1

for i in range(H):
    a[i]=[a[i][j] for j in range(W) if c[j] != 0]


for i in range(H):
    if r[i] != 0:
        print(''.join(a[i]))
