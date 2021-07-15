v = int(input())
a = list(map(int, input().split()))

i = 0
for j in range(1, len(a)):
  if a[j] <= a[i]:
    i = j

n = v // a[i]
s = a[i] * n
b = []
while s <= v:
  j = len(a) - 1
  while j > i:
    if s + (a[j] - a[i]) <= v:
      break
    j -= 1
  if j == i:
    break
  s += a[j] - a[i]
  b += [j + 1]
  
if s > 0:
  print(''.join(map(str, b + [i + 1] * (n - len(b)))))
else:
  print(-1)
