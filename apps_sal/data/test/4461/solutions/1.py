H, W = list(map(int, input().split()))

if (H%3==0) or (W%3==0):
  print((0))
else:
  ans = H * W
  H, W = min(H, W), max(H, W)
  for wi in range(1, W//2 + 1):
    S1 = H * wi
    if (H%2==0) or ((W-wi)%2==0):
      S2 = H * (W-wi) // 2
      S3 = S2
    else:
      S2 = min(H, W-wi) * (max(H, W-wi)//2)
      S3 = S2 + min(H, W-wi)
    ans = min(ans, max(S1, S2, S3) - min(S1, S2, S3))
  for hi in range(1, H//2 + 1):
    S1 = W * hi
    if (W%2==0) or ((H-hi)%2==0):
      S2 = W * (H-hi) // 2
      S3 = S2
    else:
      S2 = min(W, H-hi) * (max(W, H-hi)//2)
      S3 = S2 + min(W, H-hi)
    ans = min(ans, max(S1, S2, S3) - min(S1, S2, S3))
    
  print(ans)
  

