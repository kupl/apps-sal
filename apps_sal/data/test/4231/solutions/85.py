(H, W) = list(map(int, input().split()))
(h, w) = list(map(int, input().split()))
ans = H * W - h * W - w * H + h * w
print(ans)
