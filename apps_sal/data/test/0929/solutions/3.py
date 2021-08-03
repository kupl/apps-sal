H, W = map(int, input().split())
lsHW = []
for i in range(H):
    if i % 2 == 0:
        lsHW += list(map(int, input().split()))
    if i % 2 == 1:
        lsHW += reversed(list(map(int, input().split())))
N = 0
lsmove = []
for i in range(H * W - 1):
    if lsHW[i] % 2 == 0:
        continue
    else:
        y1 = i // W + 1
        y2 = (i + 1) // W + 1
        if (i // W) % 2 == 0:
            x1 = i % W + 1
        if (i // W) % 2 == 1:
            x1 = W - i % W
        if ((i + 1) // W) % 2 == 0:
            x2 = (i + 1) % W + 1
        if ((i + 1) // W) % 2 == 1:
            x2 = W - (i + 1) % W
        N += 1
        lsHW[i + 1] += 1
        lsmove.append([y1, x1, y2, x2])
print(N)
for i in lsmove:
    print(*i, sep=(' '))
