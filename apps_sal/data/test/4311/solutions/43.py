s = int(input())

a = []
a.append(s)
for i in range(1000000):
  if a[i]%2 == 0:
    a.append(a[i] // 2)
  else:
    a.append(3*a[i] + 1)
  for j in range(i-1):
    if a[i+1] == a[j]:
      print(len(a))
      return
