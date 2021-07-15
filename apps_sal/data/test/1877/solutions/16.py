input()
x=y=0
l=[]
s=input()
for ele in s:
  if ele=='U':
    y+=1
  else:
    x+=1
  if x>y:
    l.append(1)
  if x==y:
    l.append(l[-1])
  if x<y:
    l.append(0)
cnt=0
for i in range(1,len(l)):
  if l[i]!=l[i-1]:
    cnt+=1
print(cnt)

