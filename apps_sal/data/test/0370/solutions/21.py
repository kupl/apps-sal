k=int(input())
x,y=map(int,input().split())
if x<0:fx=-1
else:fx=1
if y<0:fy=-1
else:fy=1
ax,ay=abs(x),abs(y)
if ax<ay:
  x,y=y,x
  ax,ay=ay,ax
  fx,fy=fy,fx
  flag=1
else:flag=0
r=ax+ay
if k%2==0 and r%2==1:print(-1);return
if r==k:
  print(1)
  if flag:x,y=y,x
  print(x,y)
  return
if r%2==1 and r<k:
  print(3)
  anss=[]
  anss.append(((ax+(k-ay))//2,(k-(ax+(k-ay))//2)))
  anss.append((ax+(k-ay),0))
  anss.append((ax,ay))
  for i,j in anss:
    ii,jj=i*fx,j*fy
    if flag:ii,jj=jj,ii
    print(ii,jj)
  return
if r%2==0 and r<k:
  rm=(2*k-ax-ay)//2
else:
  rn=(k-(r%k))%k
  if rn%2==1:rn+=k
  rm=rn//2
ans=(r+rm*2)//k
anss=[]*ans
print(ans)
first=[0,-rm]
second=[ax,-rm]
third=[ax,ay]
xx=yy=0
while yy>first[1]:
  if yy-k<=first[1]:
    xx+=k-(yy-first[1])
    yy=first[1]
  else:
    yy-=k
  anss.append((xx*fx,yy*fy))
while xx<second[0]:
  if xx+k>=second[0]:
    yy+=k-(second[0]-xx)
    xx=second[0]
  else:
    xx+=k
  anss.append((xx*fx,yy*fy))
while yy!=third[1]:
  yy+=k
  anss.append((xx*fx,yy*fy))
for i,j in anss:
  ii,jj=i,j
  if flag:ii,jj=jj,ii
  print(ii,jj)
