H, W = map(int, input().split())
a = [list(input()) for _ in range(H)]
resH = [True] * H
resW = [True] * W

for h in range(H):
    judge = False
    for w in range(W):
        if a[h][w] == "#":
            judge = True
    resH[h] = judge

for w in range(W):
    judge = False
    for h in range(H):
        if a[h][w] == "#":
            judge = True
    resW[w] = judge

for h, row in enumerate(a):
    tmp = []
    for w, element in enumerate(row):
        if resH[h] and resW[w]:
            tmp.append(element)
    if tmp:
        print(*tmp, sep="")
