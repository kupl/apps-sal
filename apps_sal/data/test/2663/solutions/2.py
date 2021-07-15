n,k=list(map(int, input().split()))
a=list(map(int,input().split()))
s=[]
c=0
for i in range(1,n):
 a[i]+=a[i-1]
for i in range(n,0,-1):
 j=n
 while j-i!=0:
  ld=j-i
  m=a[ld-1]
  s.append(a[ld+i-1]-m)
  j-=1
 s.append(a[i-1])
s.sort()
for i in range(len(s)-1, len(s)-k-1,-1):
 print(s[i], end=' ')

