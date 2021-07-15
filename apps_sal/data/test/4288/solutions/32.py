A,B,C=map(int,input().split())
cnt=0
if A==B:
  cnt+=1
if A==C:
  cnt+=1
if B==C:
  cnt+=1
if cnt==1:
  print("Yes")
else:
  print("No")
