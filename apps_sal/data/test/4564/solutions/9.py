s = input()
res = "yes"
for i in range(len(s)):
  for j in range(i+1,len(s)):
    if s[i] == s[j]:
      res = "no"
print(res)
