n = int(input())
a = []
for i in range(n):
  a.append(input())
  if i > 0 and (a[i - 1][-1] != a[i][0] or a.count(a[i]) == 2):
    print("No")
    break
else:
  print("Yes")
