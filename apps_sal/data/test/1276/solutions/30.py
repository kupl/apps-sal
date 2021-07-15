N=int(input())
S=input()
SS=[]
for i in range(N):
  if S[i]=='R':SS.append(1)
  elif S[i]=='G':SS.append(2)
  else:SS.append(4)
s=0
for i in range(1,N-1):
  for j in range(1,min(i+1,N-i)):
    if SS[i-j]+SS[i]+SS[i+j]==7:
      s+=1
print(SS.count(1)*SS.count(2)*SS.count(4)-s)
