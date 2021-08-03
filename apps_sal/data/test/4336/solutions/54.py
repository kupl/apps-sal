W, H, x, y = map(int, input().split())
S = H * W / 2
res = 0
if x * 2 == W and y * 2 == H:
    res = 1
print(S, res)
