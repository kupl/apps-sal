H,W=list(map(int,input().split()))

if H%3==0 or W%3==0:
  print((0))
  return

A=0
B=0
ans=H*W

if H%2==0:
  A=H//2
  B=H//2
else:
  A=H//2+1
  B=H-A
for i in range(1,W):
  S1=A*i
  S2=B*i
  S3=(W-i)*H
  SMaxMin=max(S1,S2,S3)-min(S1,S2,S3)
  ans=min(ans,SMaxMin)
if W%2==0:
  A=W//2
  B=W//2
else:
  A=W//2+1
  B=W-A;
for i in range(1,H):
  S1=A*i
  S2=B*i
  S3=(H-i)*W
  SMaxMin=max(S1,S2,S3)-min(S1,S2,S3)
  ans=min(ans,SMaxMin)
if H>=3:
  ans=min(ans,W)
if W>=3:
  ans=min(ans,H)
print(ans)

