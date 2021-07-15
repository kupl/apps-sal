A, B = map(int, input().split())
count = 1
ans = 0
if B == 1:
  print(0)
  return
for i in range(100):
  ans += 1
  count += A - 1
  if count >= B:
    break
print(ans)
