n,h=list(map(int,input().split()))
aa=[]
bb=[]
for _ in range(n):
  a,b=list(map(int,input().split()))
  aa.append(a)
  bb.append(b)
  
maxa=max(aa)
bb.sort(reverse=True)
nage=0
ch=0
for i in range(n):
  if bb[i]>=maxa:
    nage+=bb[i]
    ch+=1
  else:
    break
    
if h>nage:
  rest=h-nage
  ch1=0
  if rest%maxa==0:
    ch1+=rest//maxa
  else:
    ch1+=(rest//maxa+1)
  print((ch1+ch))
  
else:
  ans=0
  hp=0
  for j in range(n):
    if hp>=h:
      break
    else:
      ans+=1
      hp+=bb[j]
  print(ans)
    
  

