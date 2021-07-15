n=int(input())
A=[int(i) for i in input().split()]
AA=[A[0]]
for i in range(1,n):
  AA.append(AA[-1]+A[i])
tot=AA[-1]
import bisect
ans=float("inf")
for i in range(1,n-2):
  cur=AA[i]
  l=bisect.bisect_left(AA,cur//2)
  if l==0:
    L1=[0,float("inf")]
  else:
    L1=[AA[l-1],cur-AA[l-1]]
  L2=[AA[l],cur-AA[l]]
  
  r=bisect.bisect_left(AA,cur+(tot-cur)//2)
  if r-1==i:
    R1=[0,float("inf")]
  else:
    R1=[AA[r-1]-cur,tot-AA[r-1]]
  R2=[AA[r]-cur,tot-AA[r]]
  A11=L1+R1
  A12=L1+R2
  A21=L2+R1
  A22=L2+R2
  a11=max(A11)-min(A11)
  a12=max(A12)-min(A12)
  a21=max(A21)-min(A21)
  a22=max(A22)-min(A22)

  ans=min(ans,a11,a12,a21,a22)
print(ans)
