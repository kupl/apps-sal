(H, W) = map(int, input().split())
ans = float('inf')
for h in range(1, H):
    Sa = h * W
    w = W // 2
    Sb = (H - h) * w
    Sc = (H - h) * (W - w)
    ans = min(ans, max([Sa, Sb, Sc]) - min([Sa, Sb, Sc]))
for h in range(1, H):
    Sa = h * W
    hb = (H - h) // 2
    Sb = hb * W
    Sc = (H - h - hb) * W
    ans = min(ans, max([Sa, Sb, Sc]) - min([Sa, Sb, Sc]))
for w in range(1, W):
    Sa = H * w
    h = H // 2
    Sb = h * (W - w)
    Sc = (H - h) * (W - w)
    ans = min(ans, max([Sa, Sb, Sc]) - min([Sa, Sb, Sc]))
for w in range(1, W):
    Sa = w * H
    wb = (W - w) // 2
    Sb = wb * H
    Sc = (W - w - wb) * H
    ans = min(ans, max([Sa, Sb, Sc]) - min([Sa, Sb, Sc]))
print(ans)
