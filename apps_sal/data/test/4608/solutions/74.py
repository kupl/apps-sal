n = int(input())
a = []
s = [0]*n
x = 1
for i in range(n):
  a.append(int(input()))
if 2 not in a:
  print(-1)
else:
  while True:
    if a[x-1] == 2:
      print(sum(s)+1)
      return
    else:
      s[x-1] += 1
      if s[x-1] == 2:
        print(-1)
        return
      x = a[x-1]
