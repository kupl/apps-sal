H,W,K=map(int,input().split())
C=[input()for _ in range(H)];a=0
for i in range(2**H):
 for j in range(2**W):
  b=0
  for x in range(H):
   for y in range(W):
    if(2**x&i)*(2**y&j):b+=(C[x][y]=="#")
  if b==K:a+=1
print(a)
