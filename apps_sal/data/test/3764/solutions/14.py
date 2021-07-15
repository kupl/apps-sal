n,k,x=map(int,input().split())
s=list(map(int,input().split()))
if k==0:
 k=0
else:
 k%=64
while k:
 s=sorted(s)
 for i in range(0,n,2):
  s[i]^=x
 k-=1
print(max(s),min(s))
