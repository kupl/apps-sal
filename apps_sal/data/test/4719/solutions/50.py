from collections import Counter

n=int(input())

abc='abcdefghijklmnopqrstuvwxyz'

for i in range(n):
  if i==0:
    c=Counter(input())
  else:
    c2=Counter(input())
    for k in abc:
        c[k]=min(c[k],c2[k])

ans=''
for k,v in sorted(c.items()):
  ans+=k*v

print(ans)
