a,b=map(str,input().split())
ans = a+b
if (int(ans) ** 0.5).is_integer():
  print("Yes")
else:
  print("No")
