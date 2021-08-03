import collections
W, H, x, y = map(int, input().split())

if 2 * x == W and 2 * y == H:
    tmp = 1
else:
    tmp = 0
print(W * H / 2, tmp)
