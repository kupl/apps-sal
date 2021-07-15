n=int(input())
l=sorted(map(int,input().split()))
m=l.pop()
h=m/2
t,r=h,0
for i in l:
  if (s:=abs(i-h))<t: t,r=s,i
print(m,r)
