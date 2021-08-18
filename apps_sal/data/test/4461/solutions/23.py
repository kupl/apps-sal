H, W = map(int, input().split())

ans = 10**12

for h in range(1, H):
    s1 = W * h

    h2 = (H - h) // 2
    h3 = (H - h) - h2
    s2 = W * h2
    s3 = W * h3
    max_s = max(s1, s2, s3)
    min_s = min(s1, s2, s3)
    ans = min(ans, max_s - min_s)

    w2 = W // 2
    w3 = W - w2
    s2 = (H - h) * w2
    s3 = (H - h) * w3
    max_s = max(s1, s2, s3)
    min_s = min(s1, s2, s3)
    ans = min(ans, max_s - min_s)

for w in range(1, W):
    s1 = w * H

    h2 = H // 2
    h3 = H - h2
    s2 = (W - w) * h2
    s3 = (W - w) * h3
    max_s = max(s1, s2, s3)
    min_s = min(s1, s2, s3)
    ans = min(ans, max_s - min_s)

    w2 = (W - w) // 2
    w3 = (W - w) - w2
    s2 = H * w2
    s3 = H * w3
    max_s = max(s1, s2, s3)
    min_s = min(s1, s2, s3)
    ans = min(ans, max_s - min_s)

print(ans)
