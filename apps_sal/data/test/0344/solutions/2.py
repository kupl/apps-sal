s = input()
vow = ['a', 'e', 'i', 'o', 'u']
ans = True
for i in range(len(s)):
  if s[i] not in vow:
    if s[i] != 'n':
      if i + 1 == len(s):
        ans = False
      elif s[i + 1] not in vow:
        ans = False
if ans == True:
  print("YES")
else:
  print("NO")


