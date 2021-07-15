h,w,x=map(int,input().split())
a=[list(input()) for i in range(h)]
ans=0
for i in range(2**(h+w)):
  b=0
  for j in range(h):
    for k in range(w):
      if (i>>j)&1==1 and (i>>k+h)&1==1 and a[j][k]=="#":
        b+=1
  if b==x:
    ans+=1    
print(ans)
