H, W = map(int, input().split())

ans = float("inf")
for h, w in zip([H, W], [W, H]):
    # ah の全探索
    for ah in range(1, h):
        # 残りを縦割り
        Sa = ah * w
        bw = (w - 1) // 2 + 1
        Sb = (h - ah) * bw
        Sc = (h - ah) * (w - bw)
        ans = min(ans, (max(Sa, Sb, Sc) - min(Sa, Sb, Sc)))

        # 残りを横割り
        if (h - ah) > 1:
            bh = ((h - ah) - 1) // 2 + 1
            Sb = bh * w
            Sc = (h - ah - bh) * w
            ans = min(ans, (max(Sa, Sb, Sc) - min(Sa, Sb, Sc)))

print(ans)
