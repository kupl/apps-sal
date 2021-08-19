(H, W) = map(int, input().split())
if H % 3 == 0 or W % 3 == 0:
    print(0)
elif H == 2 or W == 2:
    ans0 = min(H, W)
    (H, W) = (min(H, W), max(H, W))
    w1 = W // 3
    w2 = W - w1
    s1 = 2 * w1
    s2 = w2
    ans1 = s2 - s1
    w1 = W // 3 + 1
    w2 = W - w1
    s1 = 2 * w1
    s2 = w2
    ans2 = s1 - s2
    print(min(ans0, ans1, ans2))
else:
    ans0 = min(H, W)
    h1 = H // 2
    h2 = H - h1
    w1 = W // 3
    w2 = W - w1
    s1 = w1 * H
    s2 = w2 * h1
    s3 = w2 * h2
    ans1 = max(s1, s2, s3) - min(s1, s2, s3)
    w1 = W // 3 + 1
    w2 = W - w1
    s1 = w1 * H
    s2 = w2 * h1
    s3 = w2 * h2
    ans2 = max(s1, s2, s3) - min(s1, s2, s3)
    (H, W) = (W, H)
    h1 = H // 2
    h2 = H - h1
    w1 = W // 3
    w2 = W - w1
    s1 = w1 * H
    s2 = w2 * h1
    s3 = w2 * h2
    ans3 = max(s1, s2, s3) - min(s1, s2, s3)
    w1 = W // 3 + 1
    w2 = W - w1
    s1 = w1 * H
    s2 = w2 * h1
    s3 = w2 * h2
    ans4 = max(s1, s2, s3) - min(s1, s2, s3)
    print(min(ans0, ans1, ans2, ans3, ans4))
