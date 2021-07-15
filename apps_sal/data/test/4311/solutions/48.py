s = int(input())
S = {s}
i = 1
while True:
  i += 1
  if s % 2 == 0:
    s //= 2
  else:
    s = 3*s + 1
  if s in S:
    break
  S.add(s)
print(i)
