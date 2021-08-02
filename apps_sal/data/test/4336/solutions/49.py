W, H, x, y = map(int, input().split())

if x == W / 2 and y == H / 2:
    menseki = W * H / 2
    print(menseki, 1)
else:
    menseki = W * H / 2
    print(menseki, 0)
