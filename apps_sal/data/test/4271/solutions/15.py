n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

for i in range(n):
  if (i == 0):
    ans =b[a[0] - 1]
    y = a[0]
  else:
    x = a[i]
    if (x - y == 1):
      ans = ans + b[x - 1] + c[y - 1]
    else:
      ans = ans + b[x - 1]
    y = x

print(ans)

