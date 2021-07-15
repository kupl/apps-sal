n=int(input())
s=int(input())
ans=-1
def f(a,x):
  if a>x:
    return x
  else:
    return f(a,x//a)+(x%a)
  
for i in range(2,int(n**(1/2))+1):
  if ans<0 and f(i,n)==s:
    ans=i
  

for p in range(1,int(n**(1/2))+1)[::-1]:
  if ans<0:
    if s-p>=0 and (n+p-s)%p==0:
      b=(n+p-s)//p
      if b>=p+1 and b>=s-p+1:
        ans=b
    
if ans<0 and n==s:
  ans=(n+1)

print(ans)


  


