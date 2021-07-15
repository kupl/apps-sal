n = int(input())
a = sorted(list(map(int, input().split())))
i = n - 1
p = 0
q = 0
while i > 0:
  if a[i] == a[i-1]:
    if p == 0:
      p = a[i]
      i -= 1
    else:
      q = a[i]
      break
  i -= 1
print(p*q)
