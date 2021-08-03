H, W = map(int, input().split())
h, w = map(int, input().split())

ans = H * W - (H * w + W * h) + (h * w)
print(ans)
