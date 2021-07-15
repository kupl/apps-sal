n = int(input())
a = [int(i) for i in input().split()]
k = 0
flg = False
for ai in a:
  if ai == k + 1:
    k += 1
  else:
    flg = True
if k == 0 and flg:
  print(-1)
else:
  print(n - k)
