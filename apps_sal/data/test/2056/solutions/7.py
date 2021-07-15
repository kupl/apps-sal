n=int(input())
a=list(map(int,input().split()))
x=[0]*20
for i in range(n):
  s="{0:b}".format(a[i])
  b=[]
  for j in range(len(s)):
    b.append(s[j])
  b.reverse()
  for j in range(20-len(s)):
    b.append('0')
  b.reverse()
  for j in range(20):
    if b[j]=='1':
      x[j]+=1
ans=0
for i in range(n):
  s=[]
  for j in range(20):
    if x[j]>0:
      s.append('1')
      x[j]-=1
    else:
      s.append('0')
  ans+=int(''.join(s), 2)**2
print(ans)
