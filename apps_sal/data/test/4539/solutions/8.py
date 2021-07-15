N = int(input())
l = list(str(N))
fx = 0
for i in l:
  fx += int(i)
if N%fx == 0:
  print("Yes")
else:
  print("No")
