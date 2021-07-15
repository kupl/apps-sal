n = int(input())
t = list(map(int, input()))
a = []
for i in t:
  if i != 0:
    a.append(i)
if a == []:
  print('YES')
  return

for i in range(1, len(a)):
  sumn = sum(a[:i])
  snow = 0
  for j in range(i, len(a)):
    snow += a[j]
    if j == len(a) - 1 and snow == sumn:
      print('YES')
      return
    elif snow == sumn:
      snow = 0
    elif snow > sumn:
      break

print('NO')
