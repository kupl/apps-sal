n=int(input())
a=list(map(int,input().split()))
c1=0
s=0
for i in range(n):
  s+=a[i]
  if i%2:
    if s>=0:
      c1+=s+1
      s=-1
  else:
    if s<=0:
      c1+=-s+1
      s=1
c2=0
s=0
for i in range(n):
  s+=a[i]
  if i%2:
    if s<=0:
      c2+=-s+1
      s=1
  else:
    if s>=0:
      c2+=s+1
      s=-1
print(min(c1,c2))
