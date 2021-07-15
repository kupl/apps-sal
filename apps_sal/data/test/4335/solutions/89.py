import sys
n=int(input())
s=list(input())

if n%2!=0:
  print('No')
  return

        
a=s[:n//2]
b=s[n//2:]

cnt=0
for i in range(n//2):
  if a[i]!=b[i]:
    cnt+=1

if cnt==0:
  print('Yes')
else:
  print('No')
