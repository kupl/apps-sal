n = int(input())

tmp, nx = 0, n
while nx:
    tmp += nx%10
    nx //= 10
    
if n % tmp:
  print("No")
else:
  print("Yes")
