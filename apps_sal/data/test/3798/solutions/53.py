n=int(input())
s=int(input())
r=int(n**0.5)
for b in range(2,r+2):
  m=n
  t=0
  while m:
    t+=m%b
    m//=b
  if t==s:
    print(b)
    return
for p in range(1,r)[::-1]:
  q=s-p
  b=1+(n-s)//p
  if 1<=p<b and 0<=q<b and (n-s)%p==0:
    print(b)
    return
if n==s:
  print(n+1)
  return
print(-1)
