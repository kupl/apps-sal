H, W = map(int, input().split())

L, side, ver = [], [], []

for i in range(H):
    a = list(input())
    L.append(a)

for i in range(H):
    if ('
        side.append(L[i])

side=list(map(list, zip(*side)))

for i in range(len(side)):
    if ('
        ver.append(side[i])

ver=list(map(list, zip(*ver)))

for i in range(len(ver)):
    print(''.join(ver[i]))
