N=int(input())
A=input()
B=input()
p=1000000007
C=[1 if a == b else 0 for a,b in zip(A,B)]
if C[0]==1:
  score=3
  i=1
else:
  score=6
  i=2
while i<N:
  if C[i]==1:
    if C[i-1]==1:
    	score*=2
    i+=1
  else:
    if C[i-1]==0:
      score*=3
    else:
      score*=2
    i+=2
print(score%p)
