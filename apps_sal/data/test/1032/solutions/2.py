import sys
input=lambda: sys.stdin.readline().rstrip()
n,p=map(int,input().split())
A=sorted([int(i) for i in input().split()])
A=[A[i]-int(i) for i in range(n)]
AA=[A[-1]]
for i in range(n-1):
  AA.append(min(AA[-1],A[n-2-i]))
AA=AA[::-1]
Ans=[]
for i in range(max(A),max(A)+p+1):
  if i-AA[p-1]+1<p:
    Ans.append(i)
print(len(Ans))
print(*Ans)
