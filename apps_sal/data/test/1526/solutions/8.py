A, B, C = map(int, input().split())
c = 0
if A == B == C:
  print(0)
else:
  while(True):
    if max(A, B, C) >= 2 + min(A, B, C):
      A, B, C = max(A, B, C), A + B + C - max(A, B, C) - min(A, B, C), min(A, B, C) + 2
    else:
      A, B, C = max(A, B, C), A + B + C - max(A, B, C) - min(A, B, C) + 1, min(A, B, C) + 1
    c += 1
    if A == B == C:
      break
  print(c)
