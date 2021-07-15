n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
total = 0

for i in range(n):
  if a[i] <= b[i]:
    total += a[i]
    b[i] -= a[i]
    a[i] = 0
    if a[i+1] <= b[i]:
      total += a[i+1]
      a[i+1] = 0
    else:
      total += b[i]
      a[i+1] -= b[i]
  else:
    total += b[i]
    a[i] -= b[i]

print(total)
