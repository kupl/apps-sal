N=int(input())
S=input()

from collections import Counter
x=list(Counter(S).values())

if len(x)<3:
    print(0)
    return

c=0
for i in range(N):
 j=i+1
 for j in range(i+1,N):
  if S[i]!=S[j]:
   k=2*j-i
   if k<N and (S[k]!=S[i] and S[k]!=S[j]):c+=1
print(x[0]*x[1]*x[2]-c)
