n = int(input())
if n % 2 == 1:
  print(0)
  return
ans = 0
ex = 1
while True:
  expo = 2 * 5**ex
  if n // expo == 0:
    break
  ans += n // expo
  ex += 1
print(ans)
