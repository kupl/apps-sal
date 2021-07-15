n=int(input())
s=input()

lp=0
rp=0
for i in range(n):
  if s[i]=='(':
    rp+=1
  else:
    rp=rp-min(rp,1)
for i in range(n-1,-1,-1):
  if s[i]==')':
    lp+=1
  else:
    lp=lp-min(lp,1)

print('('*max(0,lp)+s+max(0,rp)*')')
