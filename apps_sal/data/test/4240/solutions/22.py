s=list(input())
t=list(input())

S=s+s
c=0

for i in range(len(s)):
  ch=0
  for j in range(len(s)):
    if S[i+j]==t[j]:
      ch+=1
  if ch==len(s):
    c+=1

if c>0:
  print('Yes')
  
else:
  print('No')


