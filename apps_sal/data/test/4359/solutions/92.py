L = list(int(input()) for _ in range(5))
ans = 0
for l in L:
  if l%10 != 0:
    ans += (l-(l%10))+10
  else:
    ans += l
m = 0
for l in L:
  cnt = 0
  if (l%10) == 0:
    cnt += 1
  elif m < 10-(l%10):
    m = 10-(l%10)
if cnt == 5:
  m = 0
print(ans-m)
