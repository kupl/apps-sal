import math
s=input()
n=len(s)
str=s+s
i=0
j=0
m=0
while(i<n):
  j = i
  while(j-i+1<n):
    if(str[j] != str[j+1]):
      j+=1
    else:
      break
  m=max(m,j-i+1)
  i=j+1
print(m)

