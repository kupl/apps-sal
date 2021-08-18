H, W = map(int, input().split())

ans = 1e19
for i in range(1, H):
    tate = W * i
    if i < H - 1:
        mini = W * ((H - i) // 2)
        ans = min(ans, max(tate, mini, H * W - mini - tate) - min(tate, mini, H * W - mini - tate))

    mini = (H - i) * (W // 2)
    ans = min(ans, max(tate, mini, H * W - tate - mini) - min(tate, mini, H * W - tate - mini))

for i in range(1, W):
    yoko = H * i
    if i < W - 1:
        mini = H * ((W - i) // 2)
        ans = min(ans, max(yoko, mini, H * W - mini - yoko) - min(yoko, mini, H * W - yoko - mini))
    mini = (W - i) * (H // 2)
    ans = min(ans, max(yoko, mini, H * W - yoko - mini) - min(yoko, mini, H * W - yoko - mini))

print(ans)
