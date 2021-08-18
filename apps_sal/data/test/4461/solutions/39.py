H, W = map(int, input().split())

ans = float("inf")
for h, w in zip([H, W], [W, H]):
    for ah in range(1, h):
        Sa = ah * w
        bw = (w - 1) // 2 + 1
        Sb = (h - ah) * bw
        Sc = (h - ah) * (w - bw)
        ans = min(ans, (max(Sa, Sb, Sc) - min(Sa, Sb, Sc)))

        if (h - ah) > 1:
            bh = ((h - ah) - 1) // 2 + 1
            Sb = bh * w
            Sc = (h - ah - bh) * w
            ans = min(ans, (max(Sa, Sb, Sc) - min(Sa, Sb, Sc)))

print(ans)
