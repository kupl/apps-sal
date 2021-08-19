(H, W) = map(int, input().split())
S = H * W
ans = S
for h in range(1, H):
    s1 = h * W
    s2 = W // 2 * (H - h)
    s3 = S - s1 - s2
    ans = min(ans, max(s1, s2, s3) - min(s1, s2, s3))
    s2 = (H - h) // 2 * W
    s3 = S - s1 - s2
    ans = min(ans, max(s1, s2, s3) - min(s1, s2, s3))
for w in range(1, W):
    s1 = H * w
    s2 = H // 2 * (W - w)
    s3 = S - s1 - s2
    ans = min(ans, max(s1, s2, s3) - min(s1, s2, s3))
    s2 = (W - w) // 2 * H
    s3 = S - s1 - s2
    ans = min(ans, max(s1, s2, s3) - min(s1, s2, s3))
print(ans)
