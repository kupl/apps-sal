s=input()

for i in range(len(s)):
  if i>0:
    if s[i]==s[i-1]:
      print(i-1+1,i+1)
      return
  if i>1:
    if s[i]==s[i-2]:
      print(i-2+1,i+1)
      return
      
print(-1,-1)
