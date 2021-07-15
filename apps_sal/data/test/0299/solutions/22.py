a=int(input())
b=input().split()

c=0
bi=0
bk=0

for i in range(len(b)):
   if i%3==0:
      c=c+int(b[i])
   elif i%3==1:
      bi=bi+int(b[i])
   elif i%3==2:
      bk=bk+int(b[i])

l=[]
l.append(c)
l.append(bi)
l.append(bk)

d=max(l)

if l.index(d)==0:
   print("chest")
elif l.index(d)==1:
   print("biceps")
else:
   print("back")

