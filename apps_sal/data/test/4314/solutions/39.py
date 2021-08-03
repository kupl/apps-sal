H, W = map(int, input().split())

a = [list(map(str, input().split())) for i in range(H)]
for i in range(H):
    a[i] = list(a[i][0])
flag = True
for i in range(H):
    for j in range(W):
        if a[H - 1 - i][j] != '.':
            flag = False
            break
    if flag:
        del(a[H - 1 - i])
    flag = True
for i in range(W):
    for j in range(len(a)):
        if a[j][W - 1 - i] != '.':
            flag = False
            break
    if flag:
        for j in range(len(a)):
            del(a[j][W - 1 - i])
    flag = True

for aaa in a:
    print("".join(aaa))
