(W, H, x, y) = map(int, input().split())
if x == W / 2 and y == H / 2:
    print(H * W / 2, 1)
else:
    print(H * W / 2, 0)
