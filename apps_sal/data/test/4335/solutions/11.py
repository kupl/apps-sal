n = int(input())
s = input()
if n % 2 == 1:
  res = "No"
else:
  if s[:n//2] == s[n//2:]:
    res = "Yes"
  else:
    res = "No"
print(res)
