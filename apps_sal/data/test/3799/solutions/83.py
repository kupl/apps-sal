s=list(input())
n=len(s)
flag=1
if n%2==0:
  flag=0
else:
  for i in range(n-2):
    if s[i]!=s[i+2]:
      flag=1
  for i in range(1,n-2):
    if s[i]!=s[i+2]:
      flag=1
if s[0]==s[n-1]:
  flag^=1
print('First' if flag==1 else 'Second')
