s=input()[::-1]
m=I=41
f=s.find('5')+1
i=s.find('0')+1
t=len(s)
if i:
 j=min(s.find('0',i)+1or I,f or I)
 if j<I:
  m=i+j-3
  if j<i:m+=1
if f:
 j=min(s.find('2')+1or I,s.find('7')+1or I)
 if j<I:
  l=f+j-3
  if j<f:l+=1
  if f==t:
   i=t-1
   while s[i-1]=='0':
    if i!=j:l+=1
    i-=1
  m=min(m,l)
print((-1,m)[m<I])

