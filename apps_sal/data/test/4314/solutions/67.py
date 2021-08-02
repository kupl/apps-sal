H, W = list(map(int, input().split()))
delh = []
delw = []

sq = [list(input()) for i in range(H)]

for j in range(H):
    temp = 0
    for k in range(W):
        if sq[j][k] == ".":
            temp += 1
    if temp == W:
        delh.append(j)

for l in range(W):
    temp = 0
    for m in range(H):
        if sq[m][l] == ".":
            temp += 1
    if temp == H:
        delw.append(l)

for n in range(len(delh)):
    del sq[delh[n]]
    for q in range(len(delh)):
        delh[q] -= 1
H -= len(delh)

for o in range(len(delw)):
    for p in range(H):
        del sq[p][delw[o]]
    for r in range(len(delw)):
        delw[r] -= 1

for s in range(H):
    print(("".join(sq[s])))
