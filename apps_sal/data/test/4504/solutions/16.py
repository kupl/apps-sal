s=str(input())
flag=0
for i in range(1,len(s)):
  s=s[:len(s)-2]
  for j in range(len(s)//2):
    if s[j]!=s[len(s)//2+j]:
      flag=1
      break
  if flag==0:
    print(len(s))
    return
  else:
    flag=0
    continue
