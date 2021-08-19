(H, W) = map(int, input().split())
a = []
for i in range(H):
    a.append([int(x) for x in input().split()])
n = 0
ans = []
for y in range(H):
    if y % 2 == 0:
        for x in range(W - 1):
            if a[y][x] & 1:
                a[y][x + 1] += 1
                n += 1
                ans.append('{} {} {} {}'.format(y + 1, x + 1, y + 1, x + 2))
        if y != H - 1 and a[y][W - 1] & 1:
            a[y + 1][W - 1] += 1
            n += 1
            ans.append('{} {} {} {}'.format(y + 1, W, y + 2, W))
    else:
        for x in range(W - 1, 0, -1):
            if a[y][x] & 1:
                a[y][x - 1] += 1
                n += 1
                ans.append('{} {} {} {}'.format(y + 1, x + 1, y + 1, x))
        if y != H - 1 and a[y][0] & 1:
            a[y + 1][0] += 1
            n += 1
            ans.append('{} {} {} {}'.format(y + 1, 1, y + 2, 1))
print(n)
print('\n'.join(ans))
