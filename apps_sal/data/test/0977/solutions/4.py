import sys
input=lambda: sys.stdin.readline().rstrip()
n,p=list(map(int,input().split()))
A=sorted([int(i) for i in input().split()])
st=A[0]
gl=2001
Ans=[]
for i in range(st,gl):
  for j,a in enumerate(A):
    if i+j<a or min(j+1,i+j-a+1)>=p:
      break
  else:
    Ans.append(i)
print(len(Ans))
print(*Ans)
    

