H, W = map(int, input().split())
h, w = map(int, input().split())

ans = max(0, H * W - h * W - H * w + h * w)
print(ans)
