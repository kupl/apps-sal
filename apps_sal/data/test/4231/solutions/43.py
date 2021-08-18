H, W = map(int, input().split())
h, w = map(int, input().split())

HW = []

for i in range(H):
    sublist = []
    for j in range(W):
        sublist.append(0)
    HW.append(sublist)


for i in range(h):
    for j in range(W):
        HW[i][j] = 1


for i in range(w):
    for j in range(H):
        if HW[j][i] == 1:
            continue
        HW[j][i] = 1

cnt = 0

for i in range(H):
    for j in range(W):
        if HW[i][j] == 0:
            cnt += 1

print(cnt)
