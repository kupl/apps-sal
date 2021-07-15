H, W = list(map(int, input().split(' ')))

ans = []

for h in range(1, H):
    r1 = h * W

    h = H - h

    r2a = h // 2 * W
    r3a = -1 * (-h // 2) * W
    r2b = W // 2 * h
    r3b = -1 * (-W // 2) * h

    ans.append(max(r1, r2a, r3a) - min(r1, r2a, r3a))
    ans.append(max(r1, r2b, r3b) - min(r1, r2b, r3b))

for w in range(1, W):
    r1 = H * w

    w = W - w

    r2a = H // 2 * w
    r3a = -1 * (-H // 2) * w
    r2b = w // 2 * H
    r3b = -1 * (-w // 2) * H

    ans.append(max(r1, r2a, r3a) - min(r1, r2a, r3a))
    ans.append(max(r1, r2b, r3b) - min(r1, r2b, r3b))

print((min(ans)))

