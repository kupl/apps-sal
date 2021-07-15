# cook your dish here
s=input()
cons=[]
vow=0
maxvow=0
for i in range(len(s)):
 if s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U':
  vow+=1
 else:
  if s[i] not in cons:
   cons.append(s[i])
  if vow>maxvow:
   maxvow=vow
  vow=0
if len(cons)>=5 and maxvow>=3:
 print('GOOD')
else:
 print('-1')
