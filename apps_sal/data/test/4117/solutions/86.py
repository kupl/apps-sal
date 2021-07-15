N=int(input())
L=list(map(int,input().split()))
result=0
for i in range(N):
  for j in range(i+1,N):
    for k in range(j+1,N):
      if (L[i]!=L[j] and L[i]!= L[k] and L[j]!=L[k]) and (L[i]<L[j]+L[k] and L[j]<L[i]+L[k] and L[k]<L[i]+L[j]):
        result+=1
print(result)
