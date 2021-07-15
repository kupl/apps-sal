n = int(input())
a = list(map(int, input().split()))
c = 0
for i in range(n):
  if a[i] == i:
    c += 1
if c < n:
  for i in range(n):
    if a[i] != i and a[a[i]] == i:
      c += 2
      break
  else:
    c += 1
print(c)
