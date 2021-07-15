a = input()
z=list(a)
l=[]
l1=[]
flag=0
flag1=0
v = ["A","E","I","O","U"]
for i in range(len(z)):
 if(i<len(z)-3):
  for j in range(i,i+3):
   if(z[j] in v and z[j] not in l):
    l.append(j)
   else:
    break
  if(len(l)==3):
   flag=1
   break
  l.clear()
for i in z:
 if(i not in v and i not in l1):
  l1.append(i)
if(len(l1)>=5):
 flag1=1
if(flag==1 and flag1==1):
 print("GOOD")
else:
 print(-1)
