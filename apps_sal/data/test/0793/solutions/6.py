n,m =[int(i) for i in input().split()]
s=[int(i) for i in input().split()]
t=[int(i) for i in input().split()]
a=[1]*(m+1)
for b in s:
  d=a[:]
  k=0
  for j,c in enumerate(t):
    d[j]=(k+d[j])%1000000007
    if b==c:
      k=(k+a[j])%1000000007
  d[-1]=(k+d[-1])%1000000007
  a=d[:]
print((a[-1]))
    

