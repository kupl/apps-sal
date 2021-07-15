H, W = list(map(int, input().split()))

ans = float('inf')

# first cut vertical
for x in range(1, W):
  S1 = x * H
  # cut vertical
  w2 = (W - x) // 2
  w3 = W - x - w2
  S2 = w2 * H
  S3 = w3 * H
  S_max = max(S1, S3)
  S_min = min(S1, S2)
  ans = min(ans, S_max - S_min)
  # cut horizontal
  h2 = H // 2
  h3 = H - h2
  S2 = (W - x) * h2
  S3 = (W - x) * h3
  S_max = max(S1, S3)
  S_min = min(S1, S2)
  ans = min(ans, S_max - S_min)
# first cut horizontal
for y in range(1, H):
  S1 = W * y
  # cut vertical
  w2 = W // 2
  w3 = W - w2
  S2 = w2 * (H - y)
  S3 = w3 * (H - y)
  S_max = max(S1, S3)
  S_min = min(S1, S2)
  ans = min(ans, S_max - S_min)
  # cut horizontal
  h2 = (H - y) // 2
  h3 = H - y - h2
  S2 = W * h2
  S3 = W * h3
  S_max = max(S1, S3)
  S_min = min(S1, S2)
  ans = min(ans, S_max - S_min)

print(int(ans))
