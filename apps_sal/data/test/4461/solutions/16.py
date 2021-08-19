H, W = map(int, input().split())

ans = 1e19
# 縦方向の探索
for i in range(1, H):
    tate = W * i  # 上から横に切る
    # 横に切る
    if i < H - 1:
        mini = W * ((H - i) // 2)  # 分割したやつ
        # print(tate,mini,H*W-mini-tate)
        ans = min(ans, max(tate, mini, H * W - mini - tate) - min(tate, mini, H * W - mini - tate))

    # 縦に切る
    mini = (H - i) * (W // 2)
    # print(tate,mini,H*W-mini-tate)
    ans = min(ans, max(tate, mini, H * W - tate - mini) - min(tate, mini, H * W - tate - mini))

# 横方向の探索
for i in range(1, W):
    yoko = H * i
    if i < W - 1:
        mini = H * ((W - i) // 2)
        # print(yoko,mini,H*W-mini-yoko)
        ans = min(ans, max(yoko, mini, H * W - mini - yoko) - min(yoko, mini, H * W - yoko - mini))
    mini = (W - i) * (H // 2)
    # print(yoko,mini,H*W-yoko-mini)
    ans = min(ans, max(yoko, mini, H * W - yoko - mini) - min(yoko, mini, H * W - yoko - mini))

print(ans)
