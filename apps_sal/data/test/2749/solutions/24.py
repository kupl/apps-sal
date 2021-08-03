H, W = map(int, input().split())
N = int(input())
alist = list(map(int, input().split()))

cmat = [[-1] * W for _ in range(H)]

x, y = 0, 0
c = 1
for a in alist:
    while a:
        # print(x,y)
        cmat[x][y] = c
        y += 1
        a -= 1

        if y == W:
            x += 1
            y = 0
    c += 1

# print(cmat)
for i in range(H):
    if i % 2 == 1:
        cmat[i].reverse()
    print(*cmat[i])
