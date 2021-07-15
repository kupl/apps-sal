def check(s):
  return s == s[::-1]

s=input()
n=len(s)

if check(s) and check(s[:(n-1)//2]) and check(s[(n+3)//2-1:n]):
  print("Yes")
else:
  print("No")
