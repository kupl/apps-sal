n=int(input())
a=list(map(int,input().split()))
d={}
sei=[]
tyo=[]
for s in a:
  if s not in d:
    d[s]=0
  d[s]+=1
  
for t in a:
  if d[t]>=2:
    tyo.append(t)
  if d[t]>=4:
    sei.append(t)
  d[t]=0
  
if len(sei)==0 and len(tyo)<=1:
  print(0)
  
else:
  tyos=0
  seis=0
  if len(tyo)>1:
    tyo=sorted(tyo)
    tyos+=tyo[-1]*tyo[-2]
  if len(sei)>0:
    sei=sorted(sei)
    seis+=sei[-1]**2
    
  print(max(tyos,seis))
