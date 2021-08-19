(W, H, x, y) = map(int, input().split())
print(W * H / 2, 1 if int(2 * x == W and 2 * y == H) else 0)
