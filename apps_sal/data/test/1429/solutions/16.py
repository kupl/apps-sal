N,S=list(map(str,input().split()))
N=int(N)

ans=0
for i in range(N):
  A = {"A":0,"T":0,"G":0,"C":0}
  for j in range(i,N):
    A[S[j]]+=1
    if A["A"]==A["T"] and A["G"]==A["C"]:
      ans+=1
print(ans)

