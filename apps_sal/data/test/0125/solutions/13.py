L, S, R, P = 0, 1, 2, 3
tr = []

for i in range(4):
    tr.append([int(x) for x in input().split()])

acc = False

for i in range(4):
    # check l
    if tr[i][L] == 1 and (tr[i][P] == 1 or tr[(i + 3) % 4][P] == 1):
        acc = True
        break
    if tr[i][S] == 1 and (tr[i][P] == 1 or tr[(i + 2) % 4][P] == 1):
        acc = True
        break
    if tr[i][R] == 1 and (tr[i][P] == 1 or tr[(i + 1) % 4][P] == 1):
        acc = True
        break

if acc:
    print("YES")
else:
    print("NO")
