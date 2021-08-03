H, W = map(int, input().split())
h, w = map(int, input().split())

seki = H * W
print(seki - (h * W + w * H - h * w))
