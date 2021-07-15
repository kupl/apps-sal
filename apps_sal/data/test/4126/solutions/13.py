s = input()
n = len(s)
if s != s[::-1]:
  print("No")
elif s[0:(n-1)//2] != s[(n-1)//2-1::-1]:
  print("No")
elif s[(n+3)//2-1:n] != s[n-1:(n+3)//2-2:-1]:
  print("No")
else:
  print("Yes")
