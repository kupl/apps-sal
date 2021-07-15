n,k=map(int, input().split())
a=list(map(int, input().split()))
s=input('')
b=[]
c=[]
su=0
for i in range(n):
  if len(b)==0:
    b.append(s[i])
    c.append(a[i])
  elif b[-1] == s[i]:
    b.append(s[i])
    c.append(a[i])
  elif b[-1] != s[i]:
    c.sort(reverse=True)
    for j in range(min(k,len(c))):
      su=su+c[j]
    b=[]   
    c=[]
    b.append(s[i])
    c.append(a[i])   
c.sort(reverse=True)
for j in range(min(k,len(c))):
  su=su+c[j]
print(su)  
