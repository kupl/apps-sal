n = int(input())
ks = []
for i in range(100001):
  ks.append(-1)
v = True
for i in range(n):
  x, k = list(map(int, input().split()))
  if v:
    if x > ks[k] + 1:
      v = False
    elif x > ks[k]:
      ks[k] = x

if v:
  print("YES")
else:
  print("NO")

