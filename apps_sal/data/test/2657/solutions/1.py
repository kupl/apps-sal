n=int(input())
l=sorted(map(int,input().split()))
m=l.pop()
t=h=m/2
r=0
for i in l:
  if (s:=abs(i-h))<t: t,r=s,i
print(m,r)
