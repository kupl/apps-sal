A, B, C = map(int, input().split())

ans = C - (A - B)
if ans >= 0:
  print(ans)
else:
  print(0)
