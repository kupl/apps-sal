H, A = map(int, input().split())
ans = H // A
if H % A != 0:
  ans = ans + 1
print(ans)
