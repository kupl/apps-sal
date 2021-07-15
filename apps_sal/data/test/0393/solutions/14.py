n = int(input())
s = input()

ans = "Yes"
if n == 1:
  if s == '0':
    ans = "No"
else:
  if s[0] == s[1]:
    ans = "No"
  if s[-1] == s[-2]:
    ans = "No"
  for i in range(1, n - 1):
    if s[i] == '1' and (s[i - 1] == '1' or s[i + 1] == '1'):
      ans = "No"
    if s[i] == '0' and s[i - 1] == '0' and s[i + 1] == '0':
      ans = "No"
    
print(ans)    
