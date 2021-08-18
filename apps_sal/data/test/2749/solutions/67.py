H, W = map(int, input().split())
N = int(input())
alist = list(map(int, input().split()))

cmat = []
for i in range(H):
    cmat.append([-1] * W)

x, y = 0, 0
c = 1
for a in alist:
    while a:
        if y < W:
            cmat[x][y] = c
            y += 1
            a -= 1

        if y == W:
            x += 1
            y = 0

    c += 1

for i in range(1, H, 2):
    cmat[i].reverse()

for i in range(H):
    print(*cmat[i])
