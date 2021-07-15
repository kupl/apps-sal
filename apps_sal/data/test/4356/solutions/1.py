n, m = map(int, input().split())
a, b = [], []
for i in range(n):
  a.append(input())
for i in range(m):
  b.append(input())
  
ans = False
for i in range(n-m+1):
  for j in range(n-m+1):
    flag = True
    for k in range(m):
      if a[i+k][j:j+m] != b[k]:
        flag = False
    if flag:
      ans = True

if ans:
  print("Yes")
else:
  print("No")
