H, W = map(int, input().split())
a = [list(input()) for _ in range(H)]
b = []
for i in range(H):
    if '#' in a[i]:
        b.append(a[i])
c = [[] for _ in range(len(b))]
for j in range(W):
    flag = False
    for i in range(len(b)):
        if b[i][j] == '#':
            flag = True
    if flag:
        for i in range(len(b)):
            c[i].append(b[i][j])
for i in range(len(c)):
    for j in range(len(c[i])):
        print(c[i][j], end='')
    print()
