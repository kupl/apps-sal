a, b = list(map(int, input().split()))

ans = -1
for v in range((100*10)+100):
  t8 = int(v * 0.08)
  t10 = int(v * 0.1)

  if t8 > a or t10 > b:
    break

  if t8 == a and t10 == b:
    ans = v
    break

print(ans)

