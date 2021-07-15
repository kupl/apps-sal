h,a,*m=open(0)
h,w,k,a,b,f,g=map(int,(h+a).split())
d=[I:=h*w]*I
m+=d,
q=[a:=~w+a*w+b]
d[a]=1
for s in q:
 for y,x in(1,0),(-1,0),(0,1),(0,-1):
  for z in range(k):
   if'.'!=m[(i:=s//w+y*~z)][(j:=s%w+x*~z)]or d[s]>=d[(t:=i*w+j)]:break
   if-~d[s]<d[t]:q+=t,;d[t]=d[s]+1
print(d[~w+f*w+g]%I-1)
