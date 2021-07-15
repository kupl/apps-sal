n=input()
d={}
d['a']=1
d['i']=1
d['o']=1
d['e']=1
d['u']=1
f=0
for i in range(len(n)):
  if(n[i] not in d and n[i]!='n'):
    if(i+1<len(n)):
      if(n[i+1] not in d):
        f=1
    else:
      f=1
if(f==1):
  print("NO")
else:
  print("YES")
