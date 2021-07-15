H, W = map(int, input().split())
if (H%3) * (W%3) == 0:
  print(0)
  return

ans = min(H, W)
w1 = W // 2
w2 = W - w1
S1 = (H - 1) * w1
S2 = (H - 1) * w2
S3 = W
for i in range(H-1):
  diff = max(S1, S2, S3) - min(S1, S2, S3)
  ans = min(ans, diff)
  S1 -= w1; S2 -= w2; S3 += W

h1 = H // 2
h2 = H - h1
S1 = (W - 1) * h1
S2 = (W - 1) * h2
S3 = H
for i in range(W-1):
  diff = max(S1, S2, S3) - min(S1, S2, S3)
  ans = min(ans, diff)
  S1 -= h1; S2 -= h2; S3 += H

print(ans)
