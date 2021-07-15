s = list(input())
t = list(input())
s = sorted(s)
t = sorted(t,reverse = True)
if "".join(s) < "".join(t):
  print("Yes")
else:
  print("No")
