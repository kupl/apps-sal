n=int(input())
s=set(map(int,input().split()))
m=max(s)
p=0
for x in s:
 d=1
 while x+d<=m:
  y=x+d
  if y in s:
   p=x,y
   if y+d in s:
    print(3);print(x,y,y+d);return
  d*=2
if p:
 print(2);print(*p)
else:print('1\n'+str(m))
