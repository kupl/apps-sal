H, W = map(int, input().split())
if (H % 3) * (W % 3) == 0:
    print(0)
    return

ans = H * W
w1 = W // 2
w2 = W - w1
S1 = (H - 1) * w1
T1 = W * ((H - 1) // 2)
S2 = (H - 1) * w2
T2 = W * (H - 1) - T1
S3 = W
h = H - 1
for i in range(H - 1):
    diff1 = max(S1, S2, S3) - min(S1, S2, S3)
    diff2 = max(T1, T2, S3) - min(T1, T2, S3)
    ans = min(ans, diff1, diff2)
    S1 -= w1
    S2 -= w2
    S3 += W
    h -= 1
    T1 = W * (h // 2)
    T2 = W * h - T1

h1 = H // 2
h2 = H - h1
S1 = (W - 1) * h1
T1 = H * ((W - 1) // 2)
S2 = (W - 1) * h2
T2 = H * (W - 1) - T1
S3 = H
w = W - 1
for i in range(W - 1):
    diff1 = max(S1, S2, S3) - min(S1, S2, S3)
    diff2 = max(T1, T2, S3) - min(T1, T2, S3)
    ans = min(ans, diff1, diff2)
    S1 -= h1
    S2 -= h2
    S3 += H
    w -= 1
    T1 = H * (w // 2)
    T2 = H * w - T1

print(ans)
