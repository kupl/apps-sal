n=int(input())
s=list(str(n))
for i in range(len(s)):
  s[i]=int(s[i])
b=sum(s)
a=n%b

if a==0:
  print('Yes')
else:
  print('No')
